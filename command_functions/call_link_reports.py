#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 14:01:19 2020

@author: apn
"""
from shelve_database.csv_file import csv_file
from shelve_database.json_file import json_file
from shelve_database.print_link_reports import print_link_reports
from shelve_database.yaml_file import yaml_file
import config

def call_link_reports(args) ->None:
    """
    This function delegates the task of printing the a single  cralwed report in a suitable format
    """

    if not args['no_cmd']:
        print_link_reports(args['report-id'])
    if args['yaml']:
        yaml_file(args['report-id'])
    if args['csv']:
        csv_file(args['report-id'])
    if args['json']:
        json_file(args['report-id']) 

    config.logger.info("Link Report generated according to the format chosen by user")
