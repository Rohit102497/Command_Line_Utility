import shelve
import yaml
import os
import config

def yaml_file(id: str) -> None:
    """
    This function prints the the crawled report of a single website in a YAML format
    """
    path = os.getcwd()
    directory = '/'.join([path, 'database'])
    db = shelve.open(f"{directory}/website_data")   
    
    try:  
        data = db[id]
        with open(f"{directory}/{id}.yaml", 'w') as file:
            data = yaml.dump(db[id], file, sort_keys= True , default_flow_style = False)
            
        print(f"{id}.yaml file is generated successfully in the {directory}")
        config.logger.info(f"{id}.yaml file is generated successfully in the {directory}")
    except:
        print("Enter a correct report-id")
        config.logger.info("Wrong report-id entered")

    db.close()