#!/usr/bin/env python3

# import libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import textwrap
import sys

# Metadata
AUTHOR = "Lucas Chen"
URL = sys.argv[1]
EXTENSION = "cpp"  # [cpp | java]
if EXTENSION == "cpp":
    FOLDER = "./c++/"
    IMPORTS = """
#include "leetcode.h"
"""
else:
    FOLDER = "./java/"
    IMPORTS = """
import java.util.*;
"""

# Imports for code

# Selenium
# driver = webdriver.Chrome()
# driver.get(URL)
# html = driver.page_source

# PhantomJS
driver = webdriver.PhantomJS()
driver.get(URL)
html = driver.execute_script("return document.documentElement.innerHTML;")

parser = BeautifulSoup(html, "lxml")

##############################################################################
#
# Extract Title, Description, and Problem number
# Break each line into separate lines if it is longer than 80 characters
#
##############################################################################

DESCRIPTION = parser.find('div', {'class': 'question-description'}).get_text(strip=True)
DESCRIPTION = "\n".join('\n'.join(textwrap.wrap(line, 80)) for line in DESCRIPTION.split("\n"))
DIFFICULTY = parser.find('span', attrs={'class': 'difficulty-label'}).text.strip()
TAGS = parser.find('div', {'id': 'tags-topics'}).text.strip()
TAGS = TAGS.replace('\n', ', ')
TITLE = "".join(word.capitalize for word in str.split(" "))
TITLE = parser.find('h3').text.strip()
NUMBER = TITLE.split('.')[0]
TITLE = TITLE.split('.', 1)[1].strip()


###############################################################################
#
# Write comments to file
#
###############################################################################

def comments():
    f = open(FOLDER + TITLE.replace(" ", "") + "." + EXTENSION, "w+")

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
    for line in IMPORTS.splitlines():
        f.write(line + "\n")
    f.write("\n")

    # Code
    f.write("public class " + TITLE.replace(" ", "") + " {\n\n")
    f.write("}")


###############################################################################
#
# Add new problem to proper place in readme table. If entry is already in the
# table, either do nothing (if language for that problem already exists) or add
# it as a new language for that entry (if language for that problem doesn't
# exist)
#
###############################################################################

def readme():
    FILENAME = TITLE.replace(" ", "") + "." + EXTENSION
    # Candidate entry for writing
    line = "|" + NUMBER + "|[" + TITLE + "](" + URL + ")|" + "[" + FOLDER[2:-1].capitalize() + "](" + FOLDER + FILENAME + ")|" + TAGS + "|" + DIFFICULTY + "|\n"

    # Fetch contents, modify it if necessary, and rewrite it
    README = open('./README.md', "r")
    contents = README.readlines()
    README.close()

    # Comment anchor demarcating where the table begins in entry
    anchor_line_no = contents.index("<!---anchor--->\n")

    for i in range(anchor_line_no + 1, len(contents)):
        if int(contents[i].split("|")[1]) == int(NUMBER):
            # If entry exists, get the file link portion of that entry. Add
            # candidate file link entry, sort, and remove duplicates.
            files = sorted(contents[i].split("|")[3].split(",") + [line.split("|")[3]])
            files = "".join(list(set(files)))
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
