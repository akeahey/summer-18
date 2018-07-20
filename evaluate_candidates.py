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

# Check input parameters 
if len(sys.argv) < 3:
    print "Please pass an input file of candidates followed by an input files of ground truth polymers\n"
    exit(-1)

# Get candidate polymers and actual polymer files
candidate_file = sys.argv[1]
groundtruth_file = sys.argv[2]

def cleanup_poly(pl):
    new_pl = pl.strip().strip(',').strip('.')
    if len(new_pl)>=2 and new_pl[0] == '(' and new_pl[len(new_pl)-1]==')':
        new_pl=new_pl.rstrip(')').lstrip('(')
    return new_pl


def read_items(ifile):
    items = []
    f = open(ifile)
    lines = f.readlines()
    for line in lines:
        poly = cleanup_poly(line.strip("\n"))
        upoly = u'%s' % (poly)
        items.append(upoly)
    return items

candidate_polymers = read_items(candidate_file)
extracted_polymers = read_items(groundtruth_file)

print len(candidate_polymers)
print len(extracted_polymers)

groundtruth_polymers = [x.strip().lower() for x in extracted_polymers]
groundtruth_polymers = list(set(groundtruth_polymers))
print "Number of polymer names in the dictionary: ", len(groundtruth_polymers)

candidate_polymers = [x.strip().lower() for x in candidate_polymers]
candidate_polymers = list(set(candidate_polymers))
print "Number of candidate polymers in this file: ", (len(candidate_polymers))


# Perform evaluation (compute truth positives, false positives and false negatives)
TP = 0
FP = 0
for candidate in candidate_polymers:
    if candidate in groundtruth_polymers:
        TP = TP + 1
    else:
        FP = FP + 1

precision = (TP/(TP+FP)*100)

FN = 0
for poly in groundtruth_polymers:
    if poly not in candidate_polymers:
        FN = FN + 1

recall = (TP/(TP+FN)*100)
print "True pos: ", TP
print "False pos: ", FP
print "Precision: ", precision
print "Recall: ", recall
