#!/usr/bin/env python3

# import libraries
from bs4 import BeautifulSoup
import urllib.request
import textwrap
import sys

# Metadata
AUTHOR = "Lucas Chen"
URL = sys.argv[1]
EXTENSION = "java"


# Imports for code
JAVA_IMPORTS = """
import java.util.*;
"""

# Use BeautifulSoup html parser
user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
headers = {'User-Agent': user_agent, }
request = urllib.request.Request(URL, None, headers)
page = urllib.request.urlopen(request)
parser = BeautifulSoup(page, 'html.parser')

##############################################################################
#
# Extract Title, Description, and Problem number
# Break each line into separate lines if it is longer than 80 characters
#
##############################################################################

DESCRIPTION = parser.find('div', attrs={'class': 'question-description'}).text.strip()
DESCRIPTION = "\n".join('\n'.join(textwrap.wrap(line, 80)) for line in DESCRIPTION.split("\n"))
DIFFICULTY = parser.find('span', attrs={'class': 'difficulty-label'}).text.strip()
TAGS = parser.find('div', {'id': 'tags-topics'}).text.strip()
TAGS = TAGS.replace('\n', ', ')
TITLE = "".join(word.capitalize for word in str.split(" "))
TITLE = parser.find('h3').text.strip()
NUMBER = TITLE.split('.')[0]
TITLE = TITLE.split('.', 1)[1].strip()

# print(NUMBER)
# print(TITLE)
# print(DESCRIPTION)


###############################################################################
#
# Write comments to file
#
###############################################################################

def comments():
    f = open("./java/" + TITLE.replace(" ", "") + "." + EXTENSION, "w+")

    # Header
    f.write("/*\n")
    f.write(" * " + "Solution to LeetCode Problem " + NUMBER + "\n")
    f.write(" * " + "Source: " + URL + "\n")
    f.write(" * " + "Author: " + AUTHOR + "\n")
    f.write(" */\n")
    f.write("\n")
    f.write("/*\n")

    # Description
    f.write(" * Description:\n")
    for line in DESCRIPTION.splitlines():
        f.write(" * " + line + "\n")
    f.write(" */\n")

    # Imports
    for line in JAVA_IMPORTS.splitlines():
        f.write(line + "\n")
    f.write("\n")

    # Code
    f.write("public class " + TITLE.replace(" ", "") + " {\n\n")
    f.write("}")


###############################################################################
#
# Add to readme
#
###############################################################################

def readme():
    README = open('./README.md', "a")
    FILENAME = TITLE.replace(" ", "") + "." + EXTENSION
    line = "|" + NUMBER + "|[" + TITLE + "](" + URL + ")|" + "[Java](" + "./java/" + FILENAME + ")|" + TAGS + "|" + DIFFICULTY + "|"
    README.write(line)
    print(line)


###############################################################################
#
# Get input from user
# https://stackoverflow.com/questions/3041986/apt-command-line-interface-like-yes-no-input
#
###############################################################################

def query_yes_no(question):
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}

    while True:
        print(question)
        choice = input().lower()
        if choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")


if __name__ == "__main__":
    if query_yes_no("Create file with comments? [y/n]"):
        comments()
    if query_yes_no("Add to readme? [y/n]"):
        readme()
