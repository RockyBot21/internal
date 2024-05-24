#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 24 02:44:45 2024

@author: user
"""
class MyClass:
	def __init__(self, value):
		self.value = value

	@staticmethod
	def get_max_value(x, y):
		return max(x, y)

# Create an instance of MyClass
obj = MyClass(10)

print(MyClass.get_max_value(20, 30)) 

print(obj.get_max_value(20, 30)) 

