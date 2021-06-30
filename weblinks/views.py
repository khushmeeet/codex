from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md
from .utils import parse_html_page
from newspaper import Article, Config


def save_webpage(request):
    if request.method == 'POST':
        article = Article(request.POST['url'], keep_article_html=True, fetch_images=True)
        article.download()
        article.parse()
        resp = article.article_html
        context = {
            'data': resp
        }
        return render(request, 'weblinks.html', context)
    else:
        return render(request, 'weblinks.html')
