import sys
import os
from counts import charcount, linecount, specialcount, wordcount

if len(sys.argv) != 2:
    raise Exception("Usage: python run.py filename.txt")

file_name, file_extension = os.path.splitext(sys.argv[1])

if file_extension != ".txt":
    raise Exception("Please use only plaintext files")

infile = open(sys.argv[1], "r")

#create return files
metadata_outfile = open("metadata.txt", "w")

characters = charcount(infile)
infile.seek(0)
chars_no_spaces = charcount(infile, False)
infile.seek(0)
lines = linecount(infile)
infile.seek(0)
special_punctuation = specialcount(infile)
infile.seek(0)
words = wordcount(infile)
infile.seek(0)

metadata_outfile.write(f"Characters- {characters}\n")
metadata_outfile.write(f"Characters (without spaces)- {chars_no_spaces}\n")
metadata_outfile.write(f"Lines- {lines}\n")
metadata_outfile.write(f"Special Punctuation- {special_punctuation}\n")
metadata_outfile.write(f"Words- {words}\n")