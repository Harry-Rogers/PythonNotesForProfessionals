# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:09:29 2020

@author: Harry
"""

import webbrowser
stackoverflow = "http://stackoverflow.com"
webbrowser.open(stackoverflow)
webbrowser.open_new(stackoverflow)
webbrowser.open_new_tab(stackoverflow)
ff_path = webbrowser.get("C:\Program Files\Mozilla Firefox\firefox.exe")
ff = webbrowser.get(ff_path)
ff.open(stackoverflow)