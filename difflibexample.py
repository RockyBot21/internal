#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 00:38:14 2024

@author: user
"""
import difflib

# define original text
original = "IIS 8.5 has several improvements related"

# define modified text
edited = "It has several improvements related"

# initiate the Differ object
d = difflib.Differ()

# calculate the difference between the two texts
diff = d.compare(original.split(), edited.split())

# output the result
print ('\n'.join(diff))

