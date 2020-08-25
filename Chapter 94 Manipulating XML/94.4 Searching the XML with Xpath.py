# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:17:52 2020

@author: Harry
"""

import xml.etree.cElementTree as ET

tree = ET.parse('sample.xml')
tree.findall('Books/Book')

tree.find("Books/Book[Title='The Colour of Magic']")

tree.find("Books/Book[@id='5']")

tree.find("Books/Book[2]")

tree.find("Books/Book[last()]")

tree.findall(".//Author")