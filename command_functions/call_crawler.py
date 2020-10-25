#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:28:30 2020

@author: apn
"""
from shelve_database.add_main_db import add_main_db
from shelve_database.add_website_data import add_website_data
from shelve_database.add_main_db import add_main_db
import config
from typing import Dict

def call_crawler(url) -> None:
    """
    This function takes the input URL and offers it to the web crawler module to be crawled. 
    The results from the web crawler module will indicate if the input URL is valid or broken/does not exist.
    And appropriately the crawl reports is either stored in database or an error message is prompted to the user.
    
    >>> web_crawler("htt.p://google.com")
    The given URL is broken or does not exist..
    
    """
    import os
    import sys
    
    path = os.getcwd()
    sys.path.append('/'.join([path, 'web_crawler']))
    from main import web_crawler
    
    print("Crawling", url['url'])
    config.logger.info(f"Crawling {url['url']}")
    
    results = web_crawler(url['url'])
    
    if len(results) == 1:
        config.logger.error("The given URL is broken or does not exist. Program ending..")
        config.logger.error(f"{results['error']}")
        print("The given URL is broken or does not exist. Program ending..")
        return
    else:
        config.logger.info("Crawling ended successfully")
        print(f"Found { results['number_of_links'] } links: ({ len(results['internal_references']) } internal references, { len(results['external_references']) } external references, { len(results['broken_links']) } broken links)")
        
        add_website_data(results)
        print(f"Report generated with unique-id: {results['id']}")
        config.logger.info(f"Crawled report of {results['id']} added to website_data database.")
        
        add_main_db(results)
        config.logger.info(f"Crawled report of {results['id']} added to main database.")
        
    import doctest
    doctest.testmod()