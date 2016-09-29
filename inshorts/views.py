from django.shortcuts import render
from django.http import HttpResponse
from bs4 import BeautifulSoup
import requests
import json
from django.utils.encoding import smart_str, smart_unicode

SECTION_LIST = ['national', 'business', 'sports', 'world','politics', 
                'technology', 'startup', 'entertainment', 'miscellaneous','hatke']

BASE_URL = "https://www.inshorts.com/en/read/"

NEWS_CARDS_CLASS = "news-card z-depth-1"
NEWS_CARD_IMAGE_CLASS = "news-card-image"
NEWS_CARD_TITLE_CLASS = "news-card-title"
NEWS_CARD_CONTENT = 'news-card-content'
NEWS_CARD_FOOTER = 'news-card-footer'

def get_news(request, section_name):
    if not section_name in SECTION_LIST:
        return HttpResponse("Invalid url. Please try with the proper news section")
    url = BASE_URL + section_name
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    news_cards = soup.find_all(attrs={"class":NEWS_CARDS_CLASS})
    all_news_list = []
    for news_card in news_cards:
        news_dict = get_news_info(news_card)
        all_news_list.append(news_dict)

    response = json.dumps(all_news_list, sort_keys=True, indent=4)
    return HttpResponse(response, content_type="application/json")

def get_news_info(news_card):
    news_dict = {}
    news_dict['news_title'] = smart_str(news_card.find(attrs={"class":NEWS_CARD_TITLE_CLASS}).span.text)
    news_dict['time'] = news_card.find(attrs={"class":NEWS_CARD_TITLE_CLASS}).div.find(attrs={'class':'time'})['content']
    news_dict['content'] = smart_str(news_card.find(attrs={'class':NEWS_CARD_CONTENT}).div.text)
    news_dict['full_story'] = news_card.find(attrs={'class':NEWS_CARD_FOOTER}).div.a['href']
    return news_dict


    
