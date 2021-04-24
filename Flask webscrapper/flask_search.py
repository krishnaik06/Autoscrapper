# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 12:29:21 2021

@author: win10
"""
from autoscraper import AutoScraper
from flask import Flask, request


amazon_scraper = AutoScraper()
amazon_scraper.load('amazon-search')
app = Flask(__name__)

def get_amazon_result(search_query):
    url = 'https://www.amazon.in/s?k=%s' % search_query
    result = amazon_scraper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)

def _aggregate_result(result):
    final_result = []
    print(list(result.values())[0])
    for i in range(len(list(result.values())[0])):
        try:
            
            final_result.append({alias: result[alias][i] for alias in result})
        except:
            pass
    return final_result

@app.route('/', methods=['GET'])
def search_api():
    query = request.args.get('q')
    print(query)
    return dict(result=get_amazon_result(query))

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
    
    
    
    