#!/usr/bin/python3
from files import *
import json
import os

cfg = 'tests.json'
dr = '/home/pi/Code/github/DIFF-Tool/testFiles/'

with open(cfg, 'r') as f:
    data = json.load(f)
print(data)

# single file tests
for x in data['files']:
    print("testing: {:s}{:s}".format(dr, x))
    if file_exists(dr + x):
        print("{:s} exists".format(x))
    else:
        print("{:s} doesn't exist".format(x))

    if is_file(dr + x):
        print("{:s} is a file".format(x))
    else:
        print("{:s} isn't a file".format(x))

    if file_empty(dr + x):
        print("{:s} is empty".format(x))
    else:
        print("{:s} isn't empty".format(x))

# test the sequence functions
for x in data['sequence']:
    print("testing sequence: {:s} & {:s}".format(x['f1'], x['f2']))

    if source_larger(x['f1'], x['f2']):
        print("source {:s} larger than target {:s}".format(x['f1'], x['f2']))
    else:
        if source_larger(x['f2'], x['f1']):
            print("target {:s} larger than source {:s}".format(x['f2'], x['f1']))
    
    if equal_size(x['f1'], x['f2']):
        print("(source) {:s} == (target) {:s}".format(x['f1'], x['f2']))
    else:
        print("(source) {:s} != (target) {:s}".format(x['f1'], x['f2']))
