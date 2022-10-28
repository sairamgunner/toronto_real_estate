import pandas as pd
import urllib.request
import requests
import time
# import login
import config

total_pages = 1
links = pd.DataFrame(columns=['link'])
links_done = 0

# login.loginAndBeginSession()

for page in range(1,(total_pages + 1)):
    
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    url = "https://www.zoocasa.com/toronto-on-sold-listings?page=" + str(page)
    headers={'User-Agent':user_agent,} 

    # request=urllib.request.Request(url,None,headers) #The assembled request
    # data_raw = urllib.request.urlopen(request).read()
    response = requests.get(url, headers=config.headers, cookies=config.cookies)
    print(response.status_code)
    content = response.text.encode('utf-8', 'ignore')
    with open("test.html", "w") as fp: 
        fp.write(str(content))
    # print(response.content.decode("utf-8"))
    data_split = str(response.content.decode("utf-8")).split(b'/listing-status>')[1:]
    time.sleep(1)
    
    for post in range(24): 

        try:
            start = data_split[post].find(b'href="/')
            end = data_split[post].find(b'-vow"')
            links.loc[links_done] = data_split[post][(start+7):(end+4)]
            links_done += 1
        except:
            continue

links.to_csv('house_links.csv')