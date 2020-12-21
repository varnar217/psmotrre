# -*- coding: utf-8 -*-
import requests
from selenium import webdriver
import time
import urllib
import  socket
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

import    random
#from urllib import urlopen

def get_html(URL):
    try:

        s = requests.session()
        response  =s.get(URL)
        headerss= s.cookies.get_dict()

        for  key, value in s.cookies.get_dict().items():
        #print('key=',type(key),'  value=',value)
            headerss={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
            key:value,'Upgrade-Insecure-Requests': '1', 'DNT': '1',
            'Origin': 'https://www.livelib.ru'}
            break


        rq = requests.get(URL, headers=headerss)
        rq.encoding = 'utf-8'


        time.sleep(random.randint(40, 45))

        return  rq.text
    except(requests.RequestException,ValueError):
        return False


def find_flag_next(html):
    soup=BeautifulSoup(html,'html.parser')

    next_sulka = soup.find_all('a',class_='pagination__page')
    cchar_nnext=''
    #print('next_sulka=',next_sulka)
    for sulka  in  next_sulka:
        #print('sulka=',sulka)
        if  sulka.text  =='›':
            #print(sulka)
            #print(sulka['href'])
            cchar_nnext=sulka['href']

    return  cchar_nnext

def wait_while(condition, timeout, delta=1):
    """
    @condition: lambda function which checks if the text contains "REALTIME"
    @timeout: Max waiting time
    @delta: time after which another check has to be made
    """
    max_time = time.time() + timeout
    while max_time > time.time():
        if condition():
            return True
        time.sleep(delta)
    return False

def find_all_name(html):
    soup=BeautifulSoup(html,'html.parser')

    Name_book_tag = soup.select('h1.bc__book-title')[0].text.strip()
    #Name_athor_tag = soup.select('a.bc-author__link')
    Name_athor_tag = soup.find_all('a',class_='bc-author__link')
    mean_number = soup.find('span', {'itemprop': 'ratingValue'}).get_text()
    #name_recendent = soup.find_all('a.header-card-user__name')[0].text.strip()
    name_recendent = soup.find_all('a',class_='header-card-user__name')

    recendent_number = soup.find_all('span',class_='lenta-card__mymark')
    #next_sulka = soup.find_all('span',class_='pagination__page')

    athor_name=[]
    athor_recendent=[]
    athor_recendent_nummber=[]
    for Na in Name_athor_tag:
        tetle=Na.text
        athor_name.append(tetle)

    for Na in name_recendent:
        tetle2=Na.text
        athor_recendent.append(tetle2)


    for Na in recendent_number:
        tetle3=Na.text
        athor_recendent_nummber.append(tetle3)

        return Name_book_tag, athor_name,mean_number,athor_recendent,athor_recendent_nummber


def find_all_name_all_big(html,rencedent,recenzia_number):
    soup=BeautifulSoup(html,'html.parser')

    #Name_book_tag = soup.select('h1.bc__book-title')[0].text.strip()
    #Name_athor_tag = soup.find_all('a',class_='bc-author__link')
    #mean_number = soup.find('span', {'itemprop': 'ratingValue'}).get_text()
    name_recendent = soup.find_all('a',class_='header-card-user__name')

    recendent_number = soup.find_all('span',class_='lenta-card__mymark')


    #athor_recendent=[]
    #athor_recendent_nummber=[]


    for Na in name_recendent:
        tetle2=Na.text
        rencedent.append(tetle2)


    for Na in recendent_number:
        tetle3=Na.text
        recenzia_number.append(tetle3)

        #return Name_book_tag, athor_name,mean_number,athor_recendent,athor_recendent_nummber



if __name__ =='__main__':
    i=0

    flag=True


    html=get_html("https://www.livelib.ru/book/1002455336/reviews#reviews")
    #html=get_html("https://askdev.ru/q/kod-perenapravleniya-http-3xx-v-zaprosah-python-170358/")
    #html=get_html('https://www.livelib.ru/book/1002455336/reviews/~45#reviews')
    str_23='test'+str(i)+'.html'
    #if html:
        #with open(str_23,'w',encoding='utf8') as f:
            #f.write(html)

    #name_book,athor_name,mean_number,athor_recendent,athor_recendent_nummber =find_all_name(html)
    #print(f'{name_book} , {athor_name}, {mean_number}')
    athor_recendent_nummber=[]
    athor_recendent=[]

    while(flag):
        str_23='test'+str(i)+'.html'

        if html:
            with open(str_23,'w',encoding='utf8') as f:

                f.write(html)
        i=i+1
        if i==1:
            name_book,athor_name,mean_number,athor_recendent,athor_recendent_nummber =find_all_name(html)
        else:
            find_all_name_all_big(html,athor_recendent,athor_recendent_nummber)

        next=find_flag_next(html)
        if  next=='':
            break
        #print('next=',next)

        bufer_nachalo_poisk='https://www.livelib.ru/'+str(next)
        #print('bufer_nachalo_poisk=',bufer_nachalo_poisk)
        html=get_html(bufer_nachalo_poisk)
        #if  i==38:
            #flag=False



        #if  i==1:
            #name_book,athor_name,mean_number,athor_recendent,athor_recendent_nummber =find_all_name(html,i)
        #if  i!=1:


        #print(f'{name_book} , {athor_name}, {mean_number}')
