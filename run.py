import sys
import os
from counts import charcount, linecount, specialcount, wordcount, averagelen
from sorts import commonsort, alphasort

if len(sys.argv) != 2:
    raise Exception("Usage: python run.py filename.txt")

file_name, file_extension = os.path.splitext(sys.argv[1])

if file_extension != ".txt":
    raise Exception("Please use only plaintext files")

infile = open(sys.argv[1], "r")

#create return files
metadata_outfile = open("metadata.txt", "w")
commonsort_outfile = open("commonsort.txt", "w")
alphasort_outfile = open("alphasort.txt", "w")

#write to metadata file
metadata_outfile.write(f"Characters- {charcount(infile)}\n")
metadata_outfile.write(f"Characters (without spaces)- {charcount(infile, False)}\n")
metadata_outfile.write(f"Lines- {linecount(infile)}\n")
metadata_outfile.write(f"Special Punctuation- {specialcount(infile)}\n")
metadata_outfile.write(f"Words- {wordcount(infile)}\n")
length = averagelen(infile)
metadata_outfile.write(f"Average Word Length- {format(round(length, 2))} letters\n")

#write to commonsort file
common_words = commonsort(infile)
for word in common_words:
    values = list(word.values())
    commonsort_outfile.write(f"{values[0]}- {values[1]}\n")

#TODO: Write to alphabeticalsort outfile
alphawords = alphasort(infile)
for word in alphawords:
    alphasort_outfile.write(f"{word}\n")