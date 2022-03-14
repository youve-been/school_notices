import requests
from bs4 import BeautifulSoup as bs

page = requests.get("https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1905")
soup = bs(page.text, "html.parser")

while True :
    try :
        a = soup.strong.extract()
    except :
        break

elements = soup.select('div.list_box ul > li > div > a')

for index, element in enumerate(elements, 1):
    print("{} 번째 게시글의 제목 : {}".format(index, element.string))