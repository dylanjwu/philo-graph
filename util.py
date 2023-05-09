import re

import requests
from bs4 import BeautifulSoup

base_url = 'https://en.wikipedia.org'

def get_philo_hrefs(l):
    hrefs = get_hrefs_from_ul(l)
    pattern = r'^/wiki/.*$'
    philo_hrefs = [f'{base_url}/{href}' for href in hrefs if href and re.match(pattern, href) and 'wikipedia' not in href.lower()]
    return philo_hrefs

def get_hrefs_from_ul(l):
    hrefs = [link.get('href') for link in l.find_all('a')]
    return hrefs

def get_soup(url):
    pageResponse = requests.get(url).text
    soup = BeautifulSoup(pageResponse, "html.parser")
    return soup

