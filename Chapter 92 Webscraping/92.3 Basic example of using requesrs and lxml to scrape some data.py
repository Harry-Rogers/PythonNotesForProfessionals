# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 13:54:29 2020

@author: Harry
"""

from __future__ import print_function

import lxml.html
import requests

def main():
    r = requests.get("https://httpbin.org")
    html_source = r.text
    root_element = lxml.html.fromstring(html_source)
    
    page_title = root_element.xpath('/html/head/title/text()')[0]
    print(page_title)

if __name__ == '__main__':
 main()