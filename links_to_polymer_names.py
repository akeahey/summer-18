#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TASK 1: Setup

import re
import os
import sys
import wget
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

home_dir = sys.argv[1]


#TASK 2: Parse and Follow Header Links

#narrow page down to menu header
only_menu2 = SoupStrainer(id = "menu2")
with open("scrape_page_2.html") as fp: 
	soup = BeautifulSoup(fp,'lxml', parse_only = only_menu2)
polymers = list ()

#find all 'a' tags that are part of alphabetical sorting of polymer data
a = soup.find_all("a", href = True, string = re.compile(" - "))
for _a in a: 

	#retrieve urls
	href = _a.get('href')
	y = href.split('"')
	url = "http://www.polymerdatabase.com/" + y[0]

	#download urls
	for string in url: 
		if os.path.exists(y[0]) is True:
			continue
		elif os.path.exists(y[0].replace("polymer index/", "")) is True: 
			continue
		else: 
			wget.download(url, home_dir)


#TASK 3: Parse and Follow Sub-Header Links

#narrow downloaded pages down to tables with polymer group names
	only_table = SoupStrainer ("table")
	earl = home_dir + y[0]
	with open(earl.replace("polymer index", "")) as fp: 
		soup = BeautifulSoup(fp,'lxml', parse_only = only_table)

	#find all 'a' tags that are part of polymer group names
	a = soup.find_all("a", href = True, class_ = False)
	for _a in a: 
		
		#retrieve urls
		href = _a.get('href')
		
		#exclude urls that do not link to polymer groups (ex: #.html)
		no_forbidden = len (href) > 6
		if no_forbidden == True:
			
			#standardize urls of polymer groups
			polymer_href = href.replace("polymer index/", "")

			#format urls for download
			z = polymer_href.split('"')
			url2 = "http://www.polymerdatabase.com/polymer index/" + z[0]

			#download urls
			for string in url2: 
				if os.path.exists(z[0]) is True:
					continue
				else: 
					wget.download(url2, home_dir)


#TASK 4: Extracting Polymer Names for List

			#narrow downloaded pages down to content with polymer names
			only_id_content = SoupStrainer (id = "content")
			marquis = home_dir + z[0]
			with open(marquis.replace("polymer index/", "")) as fp: 
				soup = BeautifulSoup(fp,'lxml', parse_only = only_id_content)
		
			#retrieve polymer names and add to list of polymers
			li = soup.find_all("li")
			for _li in li:
				a = _li.find_all("a")
				for _a in a:
					polymers.append(_a.get_text())

				#remove redundancies
				def remove_redundancies():
					polymers_final = list()
					for string in polymers:
						if string in polymers_final:
							continue 
						else: 
							polymers_final.append(string)
					return polymers_final


#TASK 5: Add Top 50 Polymers

polymers_list = remove_redundancies()

only_table = SoupStrainer ("table")
with open("scrape_page.html") as fp: 
	soup = BeautifulSoup(fp,'lxml', parse_only = only_table)

li = soup.find_all("li")
for _li in li:
	a = _li.find_all("a")
	for _a in a:
		polymers_list.append(_a.get_text())


#TASK 6: Turn Polymers Into File

filename = 'polymer_names.txt'
f = open(filename, 'w+')
for string in polymers_list: 
	line = '%s\n' % (string)
	f.write(line)
f.close()


