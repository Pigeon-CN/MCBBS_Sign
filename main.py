# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re  

cookie = ''''''
header = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
'Connection': 'keep-alive',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Cookie': cookie}
url = 'https://www.mcbbs.net/forum.php'
wbdata = requests.get(url,headers=header).text
soup = BeautifulSoup(wbdata,'lxml')
print(soup)
html = str(soup)
if __name__ == '__main__':  
    p = re.compile('<[^>]+>')  
    print p.sub("", html)  
    
