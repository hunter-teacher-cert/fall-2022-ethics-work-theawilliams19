# FILENAME: regex.py
# First Last: Théa Williams
# CSCI 77800 Fall 2022
# collaborators: 
# consulted: Kiana H.

import re


def find_name(line):
    pattern = r"(?:Mr. |Mrs. |Dr. |Ms. |Miss )?(?:[A-Za-z]+) ?(?:[A-Za-z\-\' ]+)*(?: Sr.| Jr.)?"
    result = re.findall(pattern,line)

    return result


f = open("names.txt")
for line in f.readlines():
    #print(line)
    result = find_name(line)
    if (len(result)>0):
        print(result)