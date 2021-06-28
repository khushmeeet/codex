from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md

def new_weblink(request):
    resp = requests.get('https://realpython.com/python-web-scraping-practical-introduction')
    soup = BeautifulSoup(resp.text, 'html.parser')
    text = ""
    for i in soup.body.descendants:
        if i.name == 'section':
            cc = ''
            for c in i.contents:
                cc += str(c)
            text += cc

    print(md(text))
    context = {
        'data': text
    }
    return render(request, 'weblinks.html', context)
