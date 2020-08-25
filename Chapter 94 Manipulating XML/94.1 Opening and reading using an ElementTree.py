# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:34:37 2020

@author: Harry
"""

import xml.etree.ElementTree as ET

tree = ET.parse("FoodMenu.xml")

root = tree.getroot()
#print all main tags
for child in root:
    print(child.tag, child.attrib)
print("\n")
#print info of tag at 0,0 and 0,1
print(root[0][0].text)
print(root[0][1].text)
#findall tags and find specific tag
print(root.findall("price"))
print(root[0].find("name"))