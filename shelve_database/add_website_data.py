import shelve 
import os
import config

path = os.getcwd()
directory = '/'.join([path, 'database'])

def add_website_data(crawled_data: dict) -> None:
    """
    This function adds a record to website_data database that holds the crawled report of a single website.
    
    """
    db = shelve.open(f"{directory}/website_data")      
    db[crawled_data['id']] = crawled_data            
    db.sync()
    config.logger.info("crawled website data added to shelve database successfully")
    db.close()