import shelve
import os
import config

def print_link_reports(id: str) -> None:
    """
    This function prints the the crawled report of a single website in a the command line
    """
  
    path = os.getcwd()
    directory = '/'.join([path, 'database'])
    db = shelve.open(f"{directory}/website_data") 

    try:
        data = db[id]
        print("report-id:", db[id]["id"])
        print("website:", db[id]["url"])
        print("total-links:", db[id]["number_of_links"])
        print("total-images:", db[id]["number_of_images"])
        
        if len(db[id]['external_references']):
            print(f"\nexternal-references ({len(db[id]['external_references'])} links):")
            print("\t# [ links-to-external-websites, response-time-in-seconds ]")
            for link in db[id]["external_references"]:
                print(f"\t-{link}")        
        
        if len(db[id]['internal_references']):
            print(f"\ninternal-references ({len(db[id]['internal_references'])} links):")
            print("\t# [ links-to-internal-webpages-and-resources, response-time-in-seconds ]")
            for link in db[id]["internal_references"]:
                print(f"\t-{link}")
                
        if len(db[id]['broken_links']):
            print(f"\nbroken-links ({len(db[id]['broken_links'])} links):")
            print("\t# [ links-that-could-not-be-resolved, http-error-status-code  ]")
            for link in db[id]["broken_links"]:
                print(f"\t-{link}")
        
        config.logger.info(f"Reports of website with report-id {id} displayed on terminal")
    except Exception as e:
        print("Enter a corect report-id")
        config.logger.info("Wrong report-id entered")
        
    db.close()