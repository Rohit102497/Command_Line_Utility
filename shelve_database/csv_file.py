import csv
import os
import shelve
import config

def truncate_file(directory):
    csvfile= open(f"{directory}csv_report.csv", 'w', newline= '') 
    csvfile.truncate()
    csvfile.close()

def csv_file(id : str) -> None:
    """
    This function prints the the crawled report of a single website in a CSV format
    """

    path = os.getcwd()
    directory = '/'.join([path, 'database']) 
    truncate_file(directory)

    db = shelve.open(f"{directory}/website_data")     
    try:
        data = db[id]
        csvfile= open(f"{directory}/{id}.csv", 'w', newline= '') 
        fieldnames = ['id', 'time_stamp', 'url', 'load_time', 'number_of_links',  'number_of_images',
                    'internal_references', 'external_references', 'broken_links' ]            
        writer = csv.DictWriter(csvfile , fieldnames = fieldnames )
        writer.writeheader()
        writer.writerow(db[id])
        csvfile.close()

        print(f"{id}.csv file is generated successfully in the {directory}")
        config.logger.info(f"{id}.csv file is generated successfully in the {directory}")
    except Exception as e:
        print("Enter a corect report-id")
        config.logger.info("Wrong report-id entered")
        
    db.close()