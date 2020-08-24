# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 12:07:33 2020

@author: Harry
"""

import scrapy
class StackOverflowSpider(scrapy.Spider):
    name = "stackoverflow" #name of spindy
    start_urls = ['http://stackoverflow.com/questions?sort=votes'] # from this url
    
    def parse(self, response): #send each response to be parsed
        
        for href in response.css('.question-summary h3 a::attr(href)'): #scrape this stuff
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback = self.parse_question)
    
    
    def parse_question(self, response):
        yield {
            'title': response.css('h1 a::text').extract_first(),
            'votes': response.css('.question .vote-count-post::text').extract_first(),
            'body': response.css('.question .post-text').extract_first(),
            'tags': response.css('.question .post-tag::text').extract(),
            'link': response.url,
            }