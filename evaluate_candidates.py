# -*- coding: utf-8 -*-
#!/usr/bin/env python
from __future__ import division
import csv
import sys
import glob
import spacy
import pandas as pd
from pandas import ExcelFile

# Load english words
nlp = spacy.load("en_core_web_sm")

# Avoid ascii error
reload(sys)
sys.setdefaultencoding('utf8')

# Get csv of candidates to evaluate
candidate_inputfile1 = sys.argv[1]
if len(sys.argv)>2:
    candidate_inputfile2 = sys.argv[2]

# Get ground truth input dir - Maybe get from user input later
input_dir = '../ground_truth/*'
# Get ground truth Excel files
ground_truth_papers = glob.glob(input_dir)

# Store all doi and corresponding polymers in a dictionary
ground_truth_papers_dict = {}

# Candidate polymers
candidate_polymers = []

def cleanup_poly(pl):
    new_pl = pl.strip().strip(',').strip('.')
    if len(new_pl)>=2 and new_pl[0] == '(' and new_pl[len(new_pl)-1]==')':
        new_pl=new_pl.rstrip(')').lstrip('(')
    return new_pl


# Read csv file (forma in notebook: doi, poly1, poly2, ...)
def readcsv(ifile):
    with open(ifile, 'rb') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            new_row = [unicode(cell, 'utf-8') for cell in row]
            new_ro = [cleanup_poly(x) for x in new_row]
            candidate_polymers.extend(new_ro[1:])
    return 

def readfasttextcandidates(ifile):
    f = open(ifile)
    lines = f.readlines()
    for line in lines:
        poly = cleanup_poly(line.strip("\n"))
        upoly = u'%s' % (poly)
        candidate_polymers.append(upoly)
    return 

# Read a single excel file
def read_excel_file(input_filename):
    df = pd.read_excel(input_filename)

    dois = []
    synthesis = []
    polymers = []
    focus = []
    count = 0
    for col in df.columns:
        if (count%2) != 0:
            #print col
            if col.find("/")!= -1:
                doi = col.split("/")[1]
            else:
                doi = col
            dois.append(doi)
            synthesis.append(df[col][0])
            doi_focus = [df[col][i] for i in range(2,len(df[col]))]
            focus.append(doi_focus)
        else:
            doi_polymers = [df[col][i] for i in range(2,len(df[col]))]
            polymers.append(doi_polymers)
        count = count + 1
    return dois,synthesis,polymers,focus

def extend_dictionary(dois, synthesis, polymers, focus):    
    for i in range(len(dois)):
        ground_truth_papers_dict[dois[i]] = {}
        ground_truth_papers_dict[dois[i]]["synthesis"] = synthesis[i]
        ground_truth_papers_dict[dois[i]]["polymers"] = polymers[i]
        ground_truth_papers_dict[dois[i]]["focus"] = focus[i]


for paper in ground_truth_papers:
    d,s,p,f = read_excel_file(paper)
    extend_dictionary(d,s,p,f)
   
# Loop through candidate file and get all polymers and
# check how many are in the ground truth

print len(ground_truth_papers_dict)
dictionary = []
for key in ground_truth_papers_dict.keys():
    dictionary.extend(ground_truth_papers_dict[key]["polymers"])
#print len(dictionary)
dictionary = list(set(dictionary))
print len(dictionary)
#dictionary.remove(nan)

for poly in dictionary:
    if isinstance(poly, float) == True:
        dictionary.remove(poly)
dictionary = [x.strip().lower() for x in dictionary]
dictionary = list(set(dictionary))
print "Number of polymer names in the dictionary: ", len(dictionary)

# Read the candidates to evaluate
readcsv(candidate_inputfile1)
if len(sys.argv)>2:
    #readfasttextcandidates(candidate_inputfile)
    readfasttextcandidates(candidate_inputfile2)
candidate_polymers = [x.strip().lower() for x in candidate_polymers]
candidate_polymers = list(set(candidate_polymers))
print "Number of candidate polymers in this file: ", (len(candidate_polymers))


TP = 0
FP = 0
for candidate in candidate_polymers:
    #ucandidate = u'%s' % candidate
    #if candidate.lower() in nlp.vocab:
    #    continue

    if candidate in dictionary:
        TP = TP + 1
    else:
        FP = FP + 1

precision = (TP/(TP+FP)*100)

FN = 0
for poly in dictionary:
    if poly not in candidate_polymers:
        FN = FN + 1

recall = (TP/(TP+FN)*100)
print "True pos: ", TP
print "False pos: ", FP
print "Precision: ", precision
print "Recall: ", recall
