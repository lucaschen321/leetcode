#!/usr/bin/env python3

# Modified from: https://github.com/mmcloughlin/problems/blob/master/leetcode/leet

import os
import sys
import argparse
import glob
import random
import logging

import requests


LOG = logging.getLogger('leet')


def problem_list(name):
    """
    Download all problems in a list.
    """
    url = 'https://leetcode.com/api/problems/' + name
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    difficulty_levels = ['easy', 'medium', 'hard']
    questions = []
    for stat_status_pair in data['stat_status_pairs']:
        question = {
            'title': stat_status_pair['stat']['question__title'],
            'titleSlug': stat_status_pair['stat']['question__title_slug'],
            'difficulty': difficulty_levels[stat_status_pair['difficulty']['level']-1],
            'paid_only': stat_status_pair['paid_only'],
            'submitted': stat_status_pair['stat']['total_submitted'],
            'accepted': stat_status_pair['stat']['total_acs'],
            'questionId': stat_status_pair['stat']['question_id']
        }
        questions.append(question)
    return questions


def question_data(title_slug):
    """
    Fetch question data from leetcode GraphQL API.
    """
    url = 'https://leetcode.com/graphql'
    payload = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": title_slug,
        },
        "query": """query questionData($titleSlug: String!) {
                question(titleSlug: $titleSlug) {
                    questionId
                    title
                    titleSlug
                    content
                    difficulty
                    likes
                    dislikes
                    codeSnippets { lang langSlug code }
                    metaData
                    topicTags { name }
                }
            }""",
    }
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()


def downloaded_title_slugs():
    """
    Get the title slugs of all problems in the current directory.
    """
    return list(map(os.path.dirname, glob.glob("*/README.md")))


def difficulty_badge(difficulty):
    subject = 'difficulty'
    status = difficulty.lower()
    color = {
        'easy': 'green',
        'medium': 'orange',
        'hard': 'red',
    }[status]
    return f'https://img.shields.io/badge/{subject}-{status}-{color}.svg?style=flat-square'


def readme_content(question):
    params = dict(question)
    params['difficulty_badge'] = difficulty_badge(question['difficulty'])

    template = '# [{title}](https://leetcode.com/problems/{titleSlug}/)\n'
    template += '<img src="{difficulty_badge}" alt="{difficulty}" />\n'
    template += '\n'
    template += '{content}\n'

    return template.format(**params)


def lang_snippet(question, lang_slug):
    for snippet in question['codeSnippets']:
        if snippet['langSlug'] == lang_slug:
            return snippet
    return None


def init_question(title_slug):
    # Fetch question data.
    response = question_data(title_slug)
    question = response['data']['question']

    """
    Create question directory with a README.
    """
    LOG.info("initializing question '%s'", title_slug)
    filename = "p{0}-{1}".format(question['questionId'].zfill(4), title_slug)
    path = "./python/{0}".format(filename)

    # Ensure the question directory exists.
    os.makedirs(path, exist_ok=True)

    # Write README.
    readme_path = os.path.join(path, 'README.md')
    content = readme_content(question)
    with open(readme_path, 'w') as f:
        f.write(content)

    readme(response)

    # Write Python snippet.
    snippet = lang_snippet(question, 'python3')
    if snippet is None:
        return
    solution_path = os.path.join(path, '{0}.py'.format(filename))
    with open(solution_path, 'w') as f:
        f.write(snippet['code'] + "\n")


def has_difficulty(difficulty):
    return lambda q: q['difficulty'] == difficulty


def difficulty_level(difficulty):
    return {'easy': 1, 'medium': 2, 'hard': 3}[difficulty]


def difficulty_at_most(difficulty):
    return lambda q: difficulty_level(q['difficulty']) <= difficulty_level(difficulty)


def difficulty_at_least(difficulty):
    return lambda q: difficulty_level(q['difficulty']) >= difficulty_level(difficulty)


def acceptance_ratio_at_least(ratio):
    return lambda q: float(q['accepted']) >= float(q['submitted']) * ratio


def submitted_at_least(min_submitted):
    return lambda q: int(q['submitted']) >= min_submitted


def not_paid_only(q):
    return not q['paid_only']


def slug_not_in(slugs):
    return lambda q: q['titleSlug'] not in slugs


def all_predicates(*predicates):
    return lambda q: all(p(q) for p in predicates)


def command_download(args):
    for title_slug in args.slug:
        init_question(title_slug)


def command_pick(args):
    # Build matching rules.
    predicates = [
        slug_not_in(downloaded_title_slugs()),
        not_paid_only,
    ]
    if args.difficulty:
        LOG.info('filter: difficulty %s', args.difficulty)
        predicates.append(has_difficulty(args.difficulty))
    if args.min_difficulty:
        LOG.info('filter: min difficulty %s', args.min_difficulty)
        predicates.append(difficulty_at_least(args.min_difficulty))
    if args.max_difficulty:
        LOG.info('filter: max difficulty %s', args.max_difficulty)
        predicates.append(difficulty_at_most(args.max_difficulty))
    if args.min_acceptance_ratio:
        LOG.info('filter: min acceptance ratio %f', args.min_acceptance_ratio)
        predicates.append(acceptance_ratio_at_least(args.min_acceptance_ratio))
    if args.min_submitted:
        LOG.info('filter: min submitted %d', args.min_submitted)
        predicates.append(submitted_at_least(args.min_submitted))
    predicate = all_predicates(*predicates)

    # Fetch and filter the problems list.
    LOG.info("choosing from list '%s'", args.list)
    questions = problem_list(args.list)
    questions = [q for q in questions if predicate(q)]

    LOG.info("%d questions available", len(questions))
    if len(questions) < args.num:
        LOG.error('not enough questions')
        return

    # Choose from them.
    chosen = random.sample(questions, args.num)
    for question in chosen:
        title_slug = question['titleSlug']
        LOG.info("picked: '%s'", title_slug)
        if not args.dry:
            init_question(title_slug)


def command_list(args):
    questions = problem_list(args.name)
    for question in reversed(questions):
        print("{questionId}. {titleSlug}".format(**question))


# "favorite_lists/top-interview-questions"
DEFAULT_LIST = "favorite_lists/top-100-liked-questions"


###############################################################################
#
# Add new problem to proper place in readme table. If entry is already in the
# table, either do nothing (if language for that problem already exists) or add
# it as a new language for that entry (if language for that problem doesn't
# exist)
#
###############################################################################

def readme(response):
    # FILENAME = TITLE.replace(" ", "") + "." + EXTENSION
    question = response['data']['question']

    filename = "p{0}-{1}".format(question['questionId'].zfill(4), question['titleSlug'])
    path = "./python/{0}/{1}.py".format(filename, filename)

    NUMBER = question['questionId']
    TITLE = question['title']
    DIFFICULTY = question['difficulty']
    TAGS = " ".join([tag['name'] for tag in question['topicTags']])
    URL = 'https://leetcode.com/problems/' + question['titleSlug']

    # Candidate entry for writing
    line = "|" + NUMBER + "|[" + TITLE + "](" + URL + ")|" + "[Python](" + path + ")|" + TAGS + "|" + DIFFICULTY + "|\n".format(NUMBER, )

    # Fetch contents, modify it if necessary, and rewrite it
    README = open('./README.md', "r")
    contents = README.readlines()
    README.close()

    # Comment anchor demarcating where the table begins in entry
    anchor_line_no = contents.index("<!---anchor--->\n")

    for i in range(anchor_line_no + 3, len(contents)):
        if int(contents[i].split("|")[1]) == int(NUMBER):
            # If entry exists, get the file link portion of that entry. Add
            # candidate file link entry, sort, and remove duplicates.
            files = [entry.strip() for entry in list(contents[i].split("|")[3].split(",") + [line.split("|")[3]])]
            files = ", ".join(sorted(list(set(files))))
            contents[i] = "|" + NUMBER + "|[" + TITLE + "](" + URL + ")|" + files + "|" + TAGS + "|" + DIFFICULTY + "|\n"
            break
        elif int(NUMBER) < int(contents[i].split("|")[1]):
            # Insert entry if it fits into middle of the table
            contents.insert(i, line)
            break
        elif i == len(contents) - 1:
            # Append entry if end of table is reached
            contents.append(line)

    README = open('./README.md', "w")
    contents = "".join(contents)
    README.write(contents)
    README.close()


def main():
    parser = argparse.ArgumentParser(description='Leetcode CLI')
    subparsers = parser.add_subparsers()

    # Define download subcommand.
    parser_download = subparsers.add_parser(
        "download", aliases=["dl", "start"], help="download problem(s)")
    parser_download.add_argument(
        'slug', nargs='+', help='title slugs to download')
    parser_download.set_defaults(action=command_download)

    # Define pick subcommand.
    parser_pick = subparsers.add_parser("pick", help="pick a problem")
    parser_pick.add_argument(
        '--list', default=DEFAULT_LIST, help='list to choose from')
    parser_pick.add_argument('--difficulty', help='difficulty')
    parser_pick.add_argument('--max-difficulty', help='maximum difficulty')
    parser_pick.add_argument('--min-difficulty', help='minimum difficulty')
    parser_pick.add_argument('--min-acceptance-ratio',
                             type=float, help='min acceptance ratio')
    parser_pick.add_argument('--min-submitted', default=100000,
                             type=int, help='min submitted')
    parser_pick.add_argument(
        '--num', type=int, default=1, help='number to choose')
    parser_pick.add_argument('--dry', action='store_true', help='dry run')
    parser_pick.set_defaults(action=command_pick)

    # Define list subcommand.
    parser_list = subparsers.add_parser(
        "list", aliases=["ls"], help="show problem list")
    parser_list.add_argument('--name', default=DEFAULT_LIST, help='list name')
    parser_list.set_defaults(action=command_list)

    # Execute.
    logging.basicConfig(level=logging.INFO)
    args = parser.parse_args()
    args.action(args)


if __name__ == '__main__':
    main()
