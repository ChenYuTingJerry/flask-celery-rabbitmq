import requests
from bs4 import BeautifulSoup
from celery import chain

from celery_worker import app
import re


@app.task(ignore_result=True)
def parse_web_links(url):
    chain(get_page.s(url), get_links.s()).apply_async()


@app.task
def get_page(url):
    html = requests.get(url).text
    return html


@app.task
def get_links(html):
    links = []
    bs = BeautifulSoup(html, features='html.parser')
    for link in bs.findAll('a', attrs={'href': re.compile("^http://|^https://")}):
        links.append(link.get('href'))
    return links
