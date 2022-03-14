import requests

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

myToken = "[봇토큰입력]"
 
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
    post_message(myToken,"#컴공_주요공지", element)

