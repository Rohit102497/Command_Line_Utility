#!/usr/bin/env python3

"""
This module receives the command line input from the user in the form:
executable_python_file arguments...
And then delegates the command functionalities to the respective action modules

"""

import argparse
from command_functions.call_crawler import call_crawler
from command_functions.call_list_reports import call_list_reports
from command_functions.call_link_reports import call_link_reports
import rlcompleter
import os
import sys
import config

path = os.getcwd()
sys.path.append('/'.join([path, 'web_crawler']))

def invalid_command() -> None:
    print("Invalid command entered..")
  
if __name__ == "__main__":
    """
    This function receives the command line arguments from the user and passes the arguments to the corresponding modules to be processed
    """

    parser = argparse.ArgumentParser("Processing input commands")

    subparsers = parser.add_subparsers(help='commands', dest = "input_command")

    # A crawl command
    crawl_parser = subparsers.add_parser('crawl', help='crawl website')
    crawl_parser.add_argument('url', help='The website url to be crawled')

    # A list-reports command
    list_reports_parser = subparsers.add_parser('list-reports', help='lists all the websites crawled')

    # A link-reports command
    link_reports_parser = subparsers.add_parser('link-reports', help='shows the statistics of the website')
    link_reports_parser.add_argument('report-id', help='report id of the website')
    link_reports_parser.add_argument('--no-cmd', action = 'store_true',
                            help='It does not prints the statistics of website in the command line')
    link_reports_parser.add_argument('--yaml', action = 'store_true',
                            help='Gives the statisctics of website in yaml format')
    link_reports_parser.add_argument('--csv', action = 'store_true',
                            help='Gives the statisctics of website in csv format')
    link_reports_parser.add_argument('--json', action = 'store_true',
                            help='Gives the statisctics of website in json format')

    arguments=parser.parse_known_args()
    config.logger.info("Arguments recieved from command line.")
    
    #argument-value dictionary
    commands = vars(arguments[0])
   
    if len(arguments[1]) != 0:   
        print("Too many arguments provided!")
        sys.exit()

    # argument-function dictionary
    functions = {
        "crawl" : call_crawler,
        "list-reports" : call_list_reports,
        "link-reports" : call_link_reports
        }
    
    if commands["input_command"] in functions:
        call_function = commands.pop('input_command')
        functions.get(call_function)(commands)
    else:
        invalid_command()    
    
    