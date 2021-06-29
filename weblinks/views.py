from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md
from .utils import parse_html_page


def save_webpage(request):
    if request.method == 'POST':
        resp = requests.get(request.POST['url'])
        soup = BeautifulSoup(resp.text, 'html.parser')
        html_text = parse_html_page(soup)
        context = {
            'data': html_text
        }
        return render(request, 'weblinks.html', context)
    else:
        return render(request, 'weblinks.html')
