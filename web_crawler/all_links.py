'''
This script prompts a user to pass the url and the first level links of the url and 
outputs dictionaries of internal, external and broken links respectively.
'''

from collections import deque
from url_html import url_html
from links_from_html import links_from_html
from typing import List, Tuple, Dict
import config

# All the extenstions that should not be crawled since they don't contain any links
dont_crawl_extensions = ('.mp3', '.deb', '.pkg', '.rar', '.rar', '.rpm',
                         '.tar.gz', '.zip', '.z', '.bin', '.dmg', '.csv', 
                         '.dat', '.db', '.log', '.mdb', '.sql', '.tar',
                        '.xml', '.email', '.vcf', '.apk', '.bat', '.cgi', 
                        '.pl', '.exe', '.jar', '.msi', '.fnt', '.otf', 
                        '.png', '.jpeg', '.ai', '.bmp', '.gif', '.jpg',
                        '.mkv', '.avi', '.tiff', '.ico', '.ps', '.tif', 
                        '.odp', '.ppt', '.pptx', '.ods', '.xls', '.xlsx', 
                        '.cfg', '.dll', '.dmp', '.ico', '.msi', '.sys', 
                        '.tmp', '.m4v','.mpg', '.wmv', '.doc', '.docx', 
                        '.pdf', '.tex', '.txt')

def all_links(links, url):
    '''
    Returns the dictionary of internal, external and broken links along with their loading
    time and error.
    '''
    queue = deque(links)
    internal = {'ref' : [], 'load_time': []}
    external= {'ref' : [], 'load_time': []}
    broken = {'ref' : [], 'err': []}
    i = 0
    while queue:
        link = queue.popleft()
        i += 1
        print(i, link)
        if link[0] == '/':
            config.logger.info(f"Checking link: {url}{link[1:]}")
            crawled_info = url_html(f"{url}{link[1:]}")
            if len(crawled_info) == 2:
                config.logger.info(f"Internal link: {url}{link[1:]}")
                internal['ref'].append(link)
                internal['load_time'].append(crawled_info[1])
                if not link.endswith(dont_crawl_extensions):
                    try: 
                        config.logger.info(f"Crawling {url}{link[1:]}")
                        html_decoded = crawled_info[0].read().decode()
                        config.logger.info("HTML of the URL decoded into a str object")
                        internal_level_links = links_from_html(html_decoded, url)
                        config.logger.info("Link is crawled and urls are added")
                        for l in internal_level_links:
                            if (l not in internal['ref'] and l not in external['ref'] 
                                    and l not in broken['ref'] and l not in queue):
                                queue.append(l)
                    except: 
                        pass
            else: 
                config.logger.info(f"Broken link: {url}{link[1:]}")
                broken['ref'].append(link)
                broken['err'].append(crawled_info[0])
        else:
            config.logger.info(f"Checking link: {link}")
            crawled_info = url_html(link)
            if len(crawled_info) == 2:
                config.logger.info(f"External link: {link}")
                external['ref'].append(link)
                external['load_time'].append(crawled_info[1])
            else:
                config.logger.info(f"Broken link: {link}")
                broken['ref'].append(link)
                broken['err'].append(crawled_info[0])
    return internal, external, broken