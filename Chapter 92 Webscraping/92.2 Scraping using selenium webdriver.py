# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 15:36:48 2020

@author: Harry
"""

from selenium import webdriver

site = 'http://stackoverflow.com/questions?sort=votes'

browser = webdriver.Firefox()

browser.get(site)

title = browser.find_element_by_css_selector('h1').text

questions = browser.find_element_by_css_selector('.question-summary')

for question in questions:
    question_title = question.find_element_by_css_selector('.summary h3 a').text
    questions_except = question.find_element_by_css_selector('.summary .excerpt').text
    question_vote = question.find_element_by_css_selector('.stats .vote .votes .vote-count-post').text
    
    print("%s\n%s\n%s votes\n-----------\n" % (question_title, questions_except, question_vote))
    
    #does not run :/