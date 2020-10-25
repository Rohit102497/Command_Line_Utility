'''
This script prompts a user to pass website url as string and outputs
a dictionay of all the links categorically present in the website.
'''

import os
import sys
import time
from typing import List
from url_html import url_html
from links_from_html import links_from_html
from all_links import all_links
from number_of_images import number_of_images

sys.path.append(os.getcwd())
import config


def links_right_format(args1: list, args2: list) -> List[list]:
    """
    Transforming two list in one by appending the elements side by side.
    Example usage:
    --------------
        >>> links_right_format([1,2,3], [a,b,c])
        [[1,a], [2,b], [3,c]]
    """
    reflist = []
    for i, j in zip(args1, args2):
        reflist.append([i, j])
    return reflist


def web_crawler(url: str) -> dict:
    """
    Returns a dictionary of all the information scrapped from a website (url) like
    number of links, number of images, the internal references, external references,
    and broken links alongwith their loading time, etc.
    It returns a dictionary containing only one field 'error' with value as the type
    of error if the url passed is invalid or broken.

    Example usage:
    --------------
        >>> url = "https://amansinha9.github.io/"

        >>> web_crawler(url)
        {'error': 'HTTP Error 404: Not Found'}
    """

    # Get the current  time stamp
    curr_clock = time.strftime(f"%Y/%m/%d %H:%M:%S {time.tzname[0]}", time.localtime())
    config.logger.info(f"Time when crawling started: {curr_clock}")
    # opening the url and getting the html code along with the loading time
    crawled_info = url_html(url)
    # While opening the url if it throws error return error else crawl the webpage
    if len(crawled_info) == 1:
        return {'error' : crawled_info[0]}

    # data will store the whole information of the website
    data = {}

    # Decode and convert the crawled html into str
    html_decoded = crawled_info[0].read().decode()
    config.logger.info("HTML of the URL decoded into a str object")

    # Get all the links from html str
    first_level_links = links_from_html(html_decoded, url)
    config.logger.info("First level links are successfully accumulated")

    # Saving the url in the dictionary
    data['url'] = url
    data['id'] = hex(hash(url))[3:9]
    data['time_stamp'] = curr_clock
    data['load_time'] = crawled_info[1]

    # Get all the links in the website and save it in data
    (data['internal_references'], data['external_references'],
     data['broken_links']) = all_links(first_level_links, url)
    config.logger.info("Internal links, External links and Broken links grouped into dictionaries")

    # Calculate the total number of links in the website
    data['number_of_links'] = (len(data['internal_references']['ref']) +
                               len(data['external_references']['ref']) +
                               len(data['broken_links']['ref']))
    config.logger.info("Total links calculated")

    # Find the number of valid images in the website
    data['number_of_images'] = number_of_images(data['internal_references'],
                                                data['external_references'])
    config.logger.info("Total images calculated")
    data["internal_references"] = links_right_format(data['internal_references']['ref'],
                                                     data['internal_references']['load_time'])
    data["external_references"] = links_right_format(data['external_references']['ref'],
                                                     data['external_references']['load_time'])
    data["broken_links"] = links_right_format(data['broken_links']['ref'],
                                              data['broken_links']['err'])
    return data

if __name__ == '__main__':
    import doctest
    doctest.testmod()
