from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from markdownify import markdownify as md
from .utils import save_html_page


def new_weblink(request):
    resp = requests.get('https://jeremycollins.net/using-a-raspberry-pi-as-a-nas-mac-os-time-machine-2020-edition')
    soup = BeautifulSoup(resp.text, 'html.parser')
    html_text = save_html_page(soup)
    context = {
        'data': html_text
    }
    return render(request, 'weblinks.html', context)
