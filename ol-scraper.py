#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2021 Luc Kusters <ljbkusters@gmail.com>
#
# Distributed under terms of the MIT license.
"""Small python based scraper for online-literature.com

Pulls books from online-literature.com and outputs them to markdown files.
"""

import argparse
import os
import requests

from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description='Pull books from'
                                             ' online-literature.com')

parser.add_argument('hyperlink', metavar='hyperlink', type=str, nargs=1,
                    help='Hyperlink to main page of the book. Like:'
                         ' http://www.online-literature.com/henry-adams/'
                         'democracy-an-american-novel')

parser.add_argument('-o --output-path', metavar="out-path", type=str, nargs=1,
                    help='Path of output directory (default ./)')
# output directory name option
parser.add_argument('-d --directory-name', metavar="dir-name", type=str, 
                    nargs=1, help='Name of output directory (default:'
                                  ' Title-Of-Book/ (dynamically dertermined))')
# path (directory) and name option
parser.add_argument('-p --path-and-name', metavar="full-path", type=str,
                    nargs=1, help='Set path and name to output directory at'
                                  ' once with one single string (instead of'
                                  ' setting output path and directory name'
                                  ' seperately.)')

# parse arguments
args = parser.parse_args()
if len(args.hyperlink) > 1:
    raise RuntimeError('Multiple links provided. This is currently not'
                       ' supported.')
LINK = args.hyperlink[0]
print(LINK)

# request and parse linked page
REQUEST = requests.get(LINK)
PARSED_HTML = BeautifulSoup(REQUEST.text, features="lxml")

# get some metadata of the page
TITLE = PARSED_HTML.body.find("span", attrs={'itemprop':'name'}).text
DIRPATH = TITLE.replace(" ", "-")
if not DIRPATH in os.listdir(os.curdir):
    os.mkdir(DIRPATH)
CHAPTERS = PARSED_HTML.body.find("div", attrs={'id':'chapters'}).find()
N_CHAPTERS = len(list(CHAPTERS.find_all("a")))

# for each chapter, write a markdown file
for i in range(1, N_CHAPTERS+1):
    print(f"Scraping chapter {i} of {N_CHAPTERS}...")
    chapter  = f"Chapter {i}"
    chapter_file_name = f"Chapter-{i}.md"
    with open(os.path.join(DIRPATH, chapter_file_name), "w") as file:
        file.write("#" + chapter)
        page_request = requests.get(f"{LINK}{i}/")
        parsed_html = BeautifulSoup(page_request.text, features="lxml") 
        chaptext_div = parsed_html.body.find("div", attrs={'id':'copy'}).find("div", attrs={"id":"chaptext"})
        for data in chaptext_div(["div"]):
            data.decompose()
        for paragraph in div:
            file.write(paragraph.text + "\n")

print("Done")
