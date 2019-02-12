# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:00:25 2019

@author: David Röbl
"""

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup


class WebText():

    def __init__(self, url: str):
        self.url = url

    def open_url(self, decoding='utf-8'):
        req = Request(self.url, headers={'User-Agent': 'Mozilla/5.0'})
        try:
            html = urlopen(req).read().decode(decoding)
            print('url opened; decoding: {}'.format(decoding))
        except UnicodeDecodeError:
            html = urlopen(req).read()
            print('url opened')

        self.soup = BeautifulSoup(html, 'lxml')

    def get_title(self):
        self.title = self.soup.title.text

    def get_all_text(self):
        pass

    def get_p_text(self):
        self.p_text = ''
        text_raw = self.soup.findAll('p')
        for i in text_raw:
            self.p_text += i.text


class PdfText():

    def __init__(self, path_pdf):
        self.path_pdf = path_pdf




