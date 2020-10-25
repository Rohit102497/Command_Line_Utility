import config
import shelve
import os

def print_list_reports() -> None:
    """
    This function prints the details of all the websites that have been crawled
    """    
    path = os.getcwd()
    directory = '/'.join([path, 'database'])
    db = shelve.open(f"{directory}/main_db")      
    index=1
    for k in db.keys():
        print(index, ".", sep="", end= " ") 
        for elem in db[k]:
            print(elem, end=" - ")   
        print()
        index += 1
       
    db.close()
    config.logger.info("List reports printed to terminal")
