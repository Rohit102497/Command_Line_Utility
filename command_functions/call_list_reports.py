#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 13:53:35 2020

@author: apn
"""

from shelve_database.print_list_reports import print_list_reports
import config

def call_list_reports(args) -> None:
    """
    This function delegates the task of printing the all the cralwed reports in a suitable format
    """
    if not args:
        config.logger.info("All the crawled reports displayed")
        print_list_reports()       
    else:
        print("Too many arguments provided")
        print('Expected ./website-stats.py list-reports')
        config.logger.error("Too many arguments provided to list-reports command")
        