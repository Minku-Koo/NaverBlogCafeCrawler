 #-*- coding: utf-8 -*-
import requests
import json
from bs4 import BeautifulSoup as bs
import os
from selenium import webdriver



## 디렉토리에서 파일 path 가져옴
def getURLFiles(path):
    filePath = os.listdir(path)
    filePath = list(map(lambda x: path + '//' + x, filePath))
    return filePath

## URL
def getContent(file):
    result = ""
    URLs = open(file, 'r', encoding="UTF-8").readlines()
    
    for URL in URLs:
        if "blog" and "naver" in URL:

            result += getNaverBlog(URL)
        else: 
            continue
    return result

def getNaverBlog(url):
    soup = getSoup(url)
    if soup:
        title = []
        content = ""
        contents = []
        try:
            url = "https://blog.naver.com" + soup.find('iframe')['src']
            soup = getSoup(url)

            title.append(soup.select_one('h3.se_textarea'))
            contents.append(soup.select('.se_textarea'))

            title.append(soup.select_one('.pcol1'))
            contents.append(soup.select('.se-main-container'))
            
            title.append(soup.select_one('.se-fs-'))
            contents.append(soup.select('.se-main-container'))
        except:
            return ""
            
        try:
            title = [i.get_text() for i in title if i != None][0]
            contents = [i for i in contents if i != None][0]
        except:
            return ""

        for c in contents:
            content += c.get_text().replace('\n', ' ') + " "
            
        return title + "\n" + content + " "
    else:
        return ""

def getNaverCafe(url):
    return ""

def getTistory(url):
    return ""

def getSoup(URL):
    try:
        res = requests.get(URL)
        soup = bs(res.text, "html.parser")
        return soup
    except:
        return False

files = getURLFiles('..//output')
for file in files:
    result = getContent(file)
    f = open(file+"_result", 'w', encoding="UTF-8")
    f.write(result)