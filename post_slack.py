from ntpath import join
import requests

#function that sends Slack messages
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

#channel and token info
posting_channel = '#컴공_주요공지'
myToken = "[token]"
 

rfp = open('titles_db.txt', 'r')


#reference : parser.py 
from bs4 import BeautifulSoup as bs

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
    
last_post = list(map(lambda s : s.rstrip(), rfp.readlines()))
    
if last_post != posting :
    for t in posting :
        if t not in last_post :
            post_message(myToken, posting_channel, t)

rfp.close()

wfp = open('titles_db.txt', 'w')
wfp.write('\n'.join(posting))
wfp.close()
