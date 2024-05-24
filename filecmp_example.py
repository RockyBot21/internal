#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 23 19:38:52 2024

@author: user
"""
# Python program to demonstrate
# filecmp.cmp() method 
import filecmp


# Path of first file
file1 = "/home/geeks/Desktop/gfg/data.txt"

# Path of second file
file2 = "/home/geeks/Desktop/gfg/gfg.txt"

# Compare the os.stat()
# signature i.e the metadata
# of both files 
comp = filecmp.cmp(file1, file2)

# Print the result of comparison
print(comp)

# Compare the
# contents of both files
comp = filecmp.cmp(file1, file2, shallow = False)

# Print the result of comparison
print(comp)
