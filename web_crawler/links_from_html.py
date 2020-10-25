'''
This script prompts a user to pass website url and the html code in string format
and output all the links present in the html in a set.
'''

import re

HREF_REGEX = r"""
    href             # Matches href command
    \s*              # Matches 0 or more white spaces
    =
    \s*             # Matches 0 or more white spaces
    [\'\"](?P<link_url>.+?)[\"\']    # Matches the url
"""

SRC_REGEX = r"""
    src
    \s*
    =
    \s*
    [\'\"](?P<src_url>.+?)[\'\"]    
"""

href_pattern = re.compile(HREF_REGEX, re.VERBOSE)
src_pattern = re.compile(SRC_REGEX, re.VERBOSE)


def links_from_html(html_crawled: str, url: str) -> set:
    '''
    Returns a set of links extracted from the html passed.
    It contains internal links by removing the url (from
    the starting of the string) passed to it.
    All internal links begins with '/'.

    Example Usage:
    --------------
        >>> url = "https://python.org/"

        >>> links_from_html('src   = "https://python.org/sitemap/"', url)
        {'/sitemap/'}

        >>> links_from_html("""src   = '#sitemap/'""", url)
        {'/#sitemap/'}

        >>> links_from_html('href   = "https://git.corp.adobe.com/"', url)
        {'https://git.corp.adobe.com/'}

    '''

    links = href_pattern.findall(html_crawled)
    links.extend(src_pattern.findall(html_crawled))
    links = set(links)
    links = {link.replace(url, "/") if link.startswith(url) else link for link in links}
    links = {f"/{link}" if link.startswith('#') else link for link in links}  
    if "/" in links:
        links.remove("/")
    return links

if __name__ == '__main__':
    import doctest
    doctest.testmod()
