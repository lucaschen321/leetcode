import os
import requests
import json


def run_graphql_query(title_slug):
    """
    Fetch question data from leetcode GraphQL API.
    """
    url = "https://leetcode.com/graphql"
    payload = {
        "operationName": "questionData",
        "variables": {
            "titleSlug": title_slug,
        },
        "query":
        """
        query questionData($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionId
            title
            titleSlug
            content
            difficulty
            isPaidOnly
            hints
            likes
            dislikes
            companyTagStats
            codeSnippets {
              lang
              langSlug
              code
            }
            metaData
            topicTags {
              name
              slug
            }
            similarQuestionList {
              difficulty
              titleSlug
              title
              translatedTitle
              isPaidOnly
            }
            mysqlSchemas
            stats
            solution {
              id
              title
              content
              contentTypeId
              paidOnly
              hasVideoSolution
              paidOnlyVideo
              canSeeDetail
              rating {
                count
                average
                userRating {
                  score
                }
              }
              topic {
                id
                commentCount
                topLevelCommentCount
                favoriteCount
                viewCount
                subscribed
                solutionTags {
                  name
                  slug
                }
                post {
                  id
                  status
                  creationDate
                  author {
                    username
                    isActive
                    profile {
                      userAvatar
                      reputation
                    }
                  }
                }
              }
            }
          }
        }
            """,
    }
    r = requests.post(url, json=payload)
    r.raise_for_status()
    return r.json()


# Set the path to the 'python' directory
python_dir = os.path.join(os.getcwd(), "python")

# Iterate over each directory under 'python'
for directory in os.listdir(python_dir):
    dir_path = os.path.join(python_dir, directory)

    # Check if the item is a directory
    if os.path.isdir(dir_path):
        # Remove the 'p****-'
        title_slug = directory.split("-", 1)[-1]

        # Run the GraphQL query
        response = run_graphql_query(title_slug)

        if response:
            # Save the response to a JSON file in the same directory
            json_file_path = os.path.join(dir_path, directory + ".json")
            with open(json_file_path, "w") as json_file:
                json.dump(response, json_file)
                print(f"Response saved to {json_file_path}")
        else:
            print(f"Failed to retrieve data for {title_slug}")
