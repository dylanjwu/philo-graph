
import json

from scrape_philo import get_philo_info
from util import get_philo_hrefs, get_soup

pages = ['https://en.wikipedia.org/wiki/List_of_philosophers_(A%E2%80%93C)',
        'https://en.wikipedia.org/wiki/List_of_philosophers_(D%E2%80%93H)',
        'https://en.wikipedia.org/wiki/List_of_philosophers_(I%E2%80%93Q)',
        'https://en.wikipedia.org/wiki/List_of_philosophers_(R%E2%80%93Z)'
        ]

def get_all_philo_urls(pages):
    philo_urls = []

    for page in pages:
        soup = get_soup(page)
        philo_hrefs = get_philo_hrefs(soup)
        philo_urls.extend(philo_hrefs)

    return philo_urls


# most_influential_philos = ['']

# urls = get_all_philo_urls(pages[:20])
# print(len(urls))

# urls = get_all_philo_urls(pages)
# urls = get_all_philo_urls(pages)[:10]
urls = ['https://en.wikipedia.org/wiki/Jean_Baudrillard']

# count = 0
# philos = []
# for href in urls:
#     philo = get_philo_info(href)
#     print(count) 
#     count += 1
#     if philo != None:
#         philos.append(philo)

# print(philos) 


def dfs(most_influential_philos):
    philos = []
    stack = most_influential_philos
    seen = set(most_influential_philos)

    while stack:
        curr = stack.pop()
        info = get_philo_info(curr)
        print(info)
        if info and info['influenced'] and info['influences']:
            philos.append(info)
            for philo in info['influenced'] + info['influences']:
                if (philo not in seen):
                    seen.add(philo)
                    stack.append(philo)
        
    return philos
            

philos = dfs(urls)

with open('data.json', 'w') as outfile:
    json.dump(philos, outfile)
