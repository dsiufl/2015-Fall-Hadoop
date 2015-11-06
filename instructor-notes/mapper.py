#!/usr/bin/env python

import sys
import os

pattern = set()
filename = os.environ['PATTERN_FILE']
if not filename:
    filename = 'pattern.txt'
f = open(filename, 'r')

for line in f:
    words = line.split()
    for word in words:
        pattern.add(word)

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # emit intermediate key-value pair
    for word in words:
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        if word in pattern:
            print '%s\t%s' % (word, 1)
