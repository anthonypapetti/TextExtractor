import sys
import os
from counts import charcount, linecount, specialcount

if len(sys.argv) != 2:
    raise Exception("Usage: python run.py filename.txt")

file_name, file_extension = os.path.splitext(sys.argv[1])

if file_extension != ".txt":
    raise Exception("Please use only plaintext files")

infile = open(sys.argv[1], "r")

print(charcount(infile), linecount(infile), specialcount(infile))