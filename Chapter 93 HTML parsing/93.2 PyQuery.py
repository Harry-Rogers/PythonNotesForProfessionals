# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 17:05:56 2020

@author: Harry
"""

from pyquery import PyQuery

html = """
<h1>Sales</h1>
<table id="table">
<tr>
 <td>Lorem</td>
 <td>46</td>
</tr>
<tr>
 <td>Ipsum</td>
 <td>12</td>
</tr>
<tr>
 <td>Dolor</td>
 <td>27</td>
</tr>
<tr>
 <td>Sit</td>
 <td>90</td>
</tr>
</table>
"""

doc = PyQuery(html)

title = doc('h1').text()

print (title)

table_data = []

rows = doc('#table > tr')

for row in rows:
 name = PyQuery(row).find('td').eq(0).text()
 value = PyQuery(row).find('td').eq(1).text()
 print ("%s\t %s" % (name, value))