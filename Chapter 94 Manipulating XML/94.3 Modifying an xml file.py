# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:02:02 2020

@author: Harry
"""

import xml.etree.ElementTree as ET

tree = ET.parse('FoodMenu.xml')

root = tree.getroot()

element = root[0]

element.set('attribute_name', 'attribute_value') #set the attribute to xml element
element.text="string_text"

tree.write('out2.xml')

root.remove(element)
tree.write('FoodMenu2.xml')