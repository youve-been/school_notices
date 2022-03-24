import requests
import schedule
import time

#function that sends Slack messages
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)

#channel and token info
posting_channel = '#컴공_학부공지'
myToken = "[bot_token]"
 
#getting infos and posting at Slack
def job():
    rfp = open('db_cs_notice2.txt', 'r')

    from bs4 import BeautifulSoup as bs

    page = requests.get("https://scc.sogang.ac.kr/front/cmsboardlist.do?siteId=cs&bbsConfigFK=1745")
    soup = bs(page.text, "html.parser")

    while True :
        try :
            a = soup.strong.extract()
        except :
            break

    elements = soup.select('div.list_box ul > li > div > a')
    posting = []
    for i in elements :
        posting.append('*'+i.get_text()+'*\n>'+'https://cs.sogang.ac.kr'+i.get('href'))
        
    db = rfp.readlines()
    last_post = []
    for idx in range(len(db)) :
        if idx % 2 == 0 :
            tmp = db[idx]+db[idx+1]
            last_post.append(tmp.rstrip())
        else :
            continue
        
    if last_post != posting :
        for t in posting :
            if t not in last_post :
                post_message(myToken, posting_channel, t)

    rfp.close()

    wfp = open('db_cs_notice2.txt', 'w', encoding='UTF-8')
    wfp.write('\n'.join(posting))
    wfp.close()

schedule.every().day.at("18:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)