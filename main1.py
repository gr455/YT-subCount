import urllib.request

import bs4 as soop

import datetime

import time

import re


def subcount():
    header={}
    header["User-Agent"]="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    new=urllib.request.Request("https://www.youtube.com/user/pewdiepie",headers=header)
    raw_data= urllib.request.urlopen(new).read()
    # ripe_data= soop.BeautifulSoup(raw_data,'html.parser')
    # data = ripe_data.find_all()  # div class="details flex-1"
    # data.append("a")
    file=open('source.txt','w')
    file.write(str(raw_data))
    file.close()

    file=open('source.txt','r')
    newstr=file.readlines()
    # print(str(newstr))
    k=0

    for z in (re.finditer("subscribers",str(newstr))):
        k=z.span()
    l=list(str(newstr))
    b=int(k[0]-11)
    c=[]
    while(b>=k[0]-11 and  b<k[1]):
        c.append(l[b])
        b+=1
    return ("".join(c))


try:
    while("true"):
        sub=subcount()
        print(sub )
        time.sleep(0);
        if(list(sub)[0]=='0'):
            hit=open("Hit_Now.txt",'a')
            hit.write(str(datetime.datetime.now()))
            hit.write("\n")
            hit.close()


except Exception as e:
    print(e)
