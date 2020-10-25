'''
This scripts prompts user to pass the website url in str format and
returns the response of the url and its loading time.
'''

import time
import urllib.request
import config

def url_html(url: str) -> list:
    """
    Returns the response of the url alongwith their loading time, etc.
    It returns a dictionary containing only one field 'error' with value
    as the type of error if the url passed is invalid or broken.

    Example usage:
    --------------
        >>> url = "https://www.linkedin.com/in/aman-sinha-756851116"

        >>> url_html(url)
        ['HTTP Error 999: Request denied']
    """

    try:
        start = time.time()
        response = urllib.request.urlopen(url)
        load_time = time.time() - start
        config.logger.info("HTML of the URL successfully parsed and returned as bytes object")
        return [response, load_time]
    
    except Exception as exp:
        config.logger.error("HTML could not be generated. Check URL..")
        return [str(exp)]



if __name__ == '__main__':
    import doctest
    doctest.testmod()
