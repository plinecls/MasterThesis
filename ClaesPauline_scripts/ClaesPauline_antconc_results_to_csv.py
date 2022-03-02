### DISCLAIMER: 
### This code was partially provided by Prof. dr. Peter Petré for an assignment of the course 'Corpus Studies' in the
### Master of Linguistics (Digital Text Analysis) and is not originally written by Pauline Claes. 


import os
import pandas as pd
import shutil
import sys
import re

script, txtdir, csvdir = sys.argv
#os.chdir(csvdir)

with open(txtdir, 'r', encoding="utf8") as sfile: # change filename to filename in question
    with open(csvdir, "w+", encoding="utf8") as tfile:
        tfile.writelines("nr\tpre\tmatch-2\tmatch-1\tmatch\tmatch+1\tmatch+2\tpost\tid\n")
        lines = sfile.readlines()
        for line in lines:
            pattern = re.compile("(\w+\W+)(\w+\W+)(\w+\W+)\t(\w+\W+)(\w+\W+)(\w+\W+)(\w+\W+)")
            line = re.sub(pattern,"\g<1>\t\g<2>\t\g<3>\t\g<4>\t\g<5>\t\g<6>\t\g<7>",line)
            pattern = re.compile("\.txt")
            line = re.sub(pattern, "", line)
            tfile.writelines(line)

#df = pd.read_csv("mps-CLEFTS.csv", encoding="utf8", sep='\t', engine="python")
#df['id'] = df['id'].astype(str)

#metadf = pd.read_csv("HansardMetaDataTexts.csv", encoding="utf8", sep="\t", engine="python")
#metadf['id'] = metadf['id'].astype(str)

#mergeddf = pd.merge(df, metadf, on="id")
#mergeddf.to_csv("mps-clefts.csv", index=False, sep='\t', encoding="utf8")
