import json
import os
import shelve
import config

def json_file(id: str) -> None:
    """
    This function prints the the crawled report of a single website in a JSON format
    """

    path = os.getcwd()
    directory = '/'.join([path, 'database'])
    db = shelve.open(f"{directory}/website_data")
    
    try:
        data = db[id]
        with open(f"{directory}/{id}.json", 'w') as json_file:
            json.dump(db[id], json_file , indent=4)

        print(f"{id}.json file is generated successfully in the {directory}")
        config.logger.info(f"{id}.json file is generated successfully in the {directory}")
    except Exception as e:
        print("Enter a corect report-id")
        config.logger.info("Wrong report-id entered")
    
    db.close()