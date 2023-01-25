import requests
from bs4 import BeautifulSoup
import csv
from retry import retry
headers = {'User-Agent':'Mozilla/5.0(Wimdows NT 6.1; WOW64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',"Connection":"close"}
k=0
@retry()#网站超时无限重试
def res_get(url):
    res = requests.get(url, headers=headers,timeout=30)
    return res
while k>=0:
    k = k+1
    url = 'http://211.146.6.141/newvideo/bvideo/play?type=episode&id={}'.format(str(k))
    res = res_get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    content = soup.select('body > div > div.content-wrapper > section > div:nth-child(2) > div > h4')
    try:  
        titles = content[0].get_text()
        print(titles)
        f=open("rt_list_2.csv","a", encoding='utf-8', newline='')
        writer=csv.writer(f)
        writer.writerow([titles, url])
        f.close()
    except:
       print("第",k,'条数据错误')