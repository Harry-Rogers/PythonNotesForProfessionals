# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 10:46:20 2020

@author: Harry
"""

import xml.etree.ElementTree as ET

p = ET.Element('parent')

c = ET.SubElement(p, 'child1')

ET.dump(p)

tree = ET.ElementTree(p)

comment = ET.Comment('user comment')
p.append(comment)

tree.write("output.xml")
