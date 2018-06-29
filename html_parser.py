#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TASK 1: Import Beautiful Soup
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
#FUNCTIONING

#TASK 2: Parsing to Table
only_table = SoupStrainer ("table")
with open("scrape_page.html") as fp: 
	soup = BeautifulSoup(fp,'lxml', parse_only = only_table)
#FUNCTIONING

#TASK 3: Extracting Polymer Names for List
polymers = list ()

li = soup.find_all("li")
for _li in li:
	a = _li.find_all("a")
	for _a in a:
		polymers.append(_a.get_text())

print(*polymers, sep = "\n")