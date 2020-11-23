import sys
import os
from counts import charcount, linecount, specialcount, wordcount
from sorts import commonsort
from santize import sanitize

if len(sys.argv) != 2:
    raise Exception("Usage: python run.py filename.txt")

file_name, file_extension = os.path.splitext(sys.argv[1])

if file_extension != ".txt":
    raise Exception("Please use only plaintext files")

infile = open(sys.argv[1], "r")

#create return files
metadata_outfile = open("metadata.txt", "w")


metadata_outfile.write(f"Characters- {charcount(infile)}\n")
metadata_outfile.write(f"Characters (without spaces)- {charcount(infile, False)}\n")
metadata_outfile.write(f"Lines- {linecount(infile)}\n")
metadata_outfile.write(f"Special Punctuation- {specialcount(infile)}\n")
metadata_outfile.write(f"Words- {wordcount(infile)}\n")

print(commonsort(infile))