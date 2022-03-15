#this file is for testing web crawling before at post_slack.py

import requests
from bs4 import BeautifulSoup as bs
import time

fp = open('titles_db.txt', 'w')

#while True :
page = requests.get("https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1905")
soup = bs(page.text, "html.parser")

while True :
    try :
        a = soup.strong.extract()
    except :
        break

elements = soup.select('div.list_box ul > li > div > a')
posting = []
for i in elements :
    posting.append('*'+i.get_text()+'*/n'+'https://cs.sogang.ac.kr'+i.get('href'))

fp.write('\n'.join(posting))
    
#testing prints
#for idx, element in enumerate(title, 1):
#    print("{} 번째 게시글의 제목 : {}".format(idx, element))
#    print("링크 : {}".format(link[idx]))
#print()

#find updates - for post_slack.py   
#if last_title != title :
#    for t in title :
#        if t not in last_title :
#            print('sth changed')
#last_title = title

#time.sleep(300)

fp.close()