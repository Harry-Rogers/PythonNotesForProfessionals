# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:39:08 2020

@author: Harry
"""


from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.codechef.com/problems/easy')
# Create a BeautifulSoup object

page = BeautifulSoup(res.text, 'lxml') # the text field contains the source of the page

datatable_tags = page.select('table.dataTable') # The problems are in the <table> tag,  with class "dataTable" extract the first tag from the list, since that's what we desire

datatable = datatable_tags[0]
# Now since we want problem names, they are contained in <b> tags, which are  directly nested under <a> tags
prob_tags = datatable.select('a > b')

prob_names = [tag.getText().strip() for tag in prob_tags]

print (prob_names)
