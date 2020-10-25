import shelve 
import os
import sys
import config

path = os.getcwd()
directory = '/'.join([path, 'database'])

def add_main_db(data: dict) -> None:
    """
    This function adds a record to main_db database that holds the reports of all the websites crawled so far.
    
    """
    db = shelve.open(f"{directory}/main_db")      
    db[data["id"]] = [data["id"], data["time_stamp"], data["url"] ]
    db.sync()
    config.logger.info("crawled data added to main database successfully..")
    db.close()