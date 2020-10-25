# website-stats - Implement a simple website statistics/benchmarking tool

## Description 
We have created a command line utility that helps us to maintain statistics of a website. The statistics of a website includes the total number of links, number of images, list of all the links it contains which includes the list of broken links, list of internal as well as external links. The stats data also consists of the loading time a website takes.

## Prerequisites

1. Latest version of python installed.(version 3.6.x or above)
2. Install the 'yaml' modue using the package manager pip.
```pip install pyyaml```

## Installation

### Clone
Clone this repo to your local machine using the [git@git.corp.adobe.com:apn/PY_3.git](git@git.corp.adobe.com:apn/PY_3.git)

### How to use it


1. Go to the directory containing ```website-stats.py``` file to pass the input commands and start with the project.
2. The file accepts ```call_crawler```or ```call_list_reports```or``` call_link_reports``` as input and with respect to each input performs a specific task.
2. The command line performs three different kinds of operations:
* crawl
* list-reports
* link-reports

## Description 

### command_functions module
This module consists of files which will make a call on the basis of the input to different functionalities.
  * ```call_crawler.py``` file makes a call to caller module each time when we have to crawl the data of a new website which isn't crawled yet.
  * ```call_list_reports.py``` file prints the list of already called websites
  * ```call_link_reports.py``` file print the statistics of a paricular website given the report-id by the user. User also have the option of generating a report in different formats like yaml, json or csv format.
### web_crawler module
This module consists of files which performs the main part of the project ie. crawling of data
  * ```main.py``` makes a call to all the data attributes which we havr to fetch and then store the data in a dictionary .
  * ```get_all_links.py``` file returns all the links crawled. 
  * ```get_links_from_html.py``` file returns internal links by removing the url passed to it. 
  * ```get_number_of_images.py``` file returns a count of the number of images in the website .
### Shelve_database module
This module consists of the backend part where the storage of data takes place in different forms. As of now, we have used shelve library for persistent storage of data.
  * ``` add_website_db.py``` and ```add_main_db.py``` files writes the data to the respective databases.
  * ``` print_link_reports.py``` and ```print_list_reports.py``` files prints the data of the respective databases.
  * ```yaml_file.py```, ```csv_file.py``` and ```json_file.py``` files are called when the user wants the reports to be generated in different formats respectively.
  
### Database module
The module consists of two databses. One database ```main_db.db``` maintains the list of crawled websites along with their report-id and time stamp. Other database ```website_data.db``` stores the data of individual websites.
## Contribution

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
