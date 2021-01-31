
# this program randomly accesses various websites
# in order to obfuscate your "profile" online
# nothing illegal is accessed, however, various political,
# religious, sexual shopping etc. websites are routinely visited
#
# the idea is that if enough people use it, it will "normalize"
# everyone and prevent online marketting and advertizing aggregators
# from creating a profile of your internet activities

import time
import random
import requests
from fake_useragent import UserAgent

# invoke every x seconds (5-60) and take your chance on visiting a random website
# chance parameter is the probability of doing something as opposed to nothing
# the idea is to randomize the access pattern
def loop(fake_browser_header, chance=10, site_list=[]):
    headers = {'User-Agent': fake_browser_header}
    try:
        c = random.randrange(0,100,1)
        print(f"Dice roll = {c}, chance = {chance}")
        if c < chance:
            # go on to visiting a random website
            # pick a website from the list
            p = random.randrange(0,len(site_list),1)
            url = site_list[p]
            print(f"Selecting url: {url}")
            r = requests.get(url, headers=headers, timeout=10)
            if r.status_code != requests.codes.ok:
                r.raise_for_status()
            # do something with response
            # then wait a random amount of time
            time_to_wait = random.randrange(5,60)
            print(f"Pausing {time_to_wait} seconds.")
            time.sleep(time_to_wait)
    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':
    try:
        site_list = []
        # prepare a fake browser agent signature
        ua = UserAgent()
        # open the site database
        with open('site-database.txt') as f:
            site_list = f.readlines()
        # remove \n from all urls
        site_list = [url[:-1] if url[-1] == '\n' else url for url in site_list]
        site_list = ['http://' + url if not url.startswith('http://') else url for url in site_list]
        # keep visiting random websites
        while True:
            loop(ua.chrome, 20, site_list)
    except Exception as e:
        print(e)
