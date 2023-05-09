

from util import get_philo_hrefs, get_soup

base_url = 'https://en.wikipedia.org'

# phil_url = 'https://en.wikipedia.org/wiki/Jean_Baudrillard'

def get_philo_info(phil_url):
    soup = get_soup(phil_url)
    influenced = get_influenced(soup)
    influences = get_influences(soup)
    if not influenced and not influences:
        return None
    return { 'philo': phil_url, 'influenced': influenced, 'influences': influences}


def get_influenced(soup):
    influenced_by_title = soup.find('div', string='Influenced')
    if not influenced_by_title or len(list(influenced_by_title.next_siblings)) < 2:
        return []
    influenced_by_list = list(influenced_by_title.next_siblings)[1]
    if influenced_by_list:
        phil_hrefs = get_philo_hrefs(influenced_by_list)
        return phil_hrefs
    return []


def get_influences(soup):
    influences_title = soup.find('div', string='Influences')
    if not influences_title or len(list(influences_title.next_siblings)) < 2:
        return []
    influences_list = list(influences_title.next_siblings)[1]
    if influences_list:
        phil_hrefs = get_philo_hrefs(influences_list)
        return phil_hrefs
    return []


# info = get_philo_info(phil_url)
# print(info)
