from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
import requests
import datetime
from markdownify import markdownify as md
from main.utils import safe_html_trim
from .utils import parse_html_page
from .models import ExternalData
from newspaper import Article, Config


def list_webpages(request):
    all_external_data = ExternalData.objects.all()
    for data in all_external_data:
        data.content = safe_html_trim(data.content)
    context = {
        'all_external_data': all_external_data
    }
    return render(request, 'main.html', context)


def save_webpage(request):
    if request.method == 'POST':
        article = Article(request.POST['url'], keep_article_html=True, fetch_images=True)
        article.download()
        article.parse()
        article_html = article.article_html
        article_title = article.title
        article_html = f'<h1>{article_title}</h1>' + article_html
        ed = ExternalData(
            content=article_html,
            url=request.POST['url'],
            added_on=datetime.datetime.now(datetime.timezone.utc),
            data_type='HTML'
        )
        ed.save()
        return redirect('notes_list')
    else:
        return render(request, 'new_html.html')
