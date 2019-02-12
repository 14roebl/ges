# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:07:51 2019

@author: David Röbl
"""

import pandas as pd
import geopandas as gpd
import re
from collections import Counter
import nltk


class administrative_boundaries():

    def __init__(self, web_text: str):
        self.web_text = web_text

    def search_and_count(self, lvl_boundaries: gpd.GeoDataFrame, name: str):
        boundaries_all = set(lvl_boundaries['name'])
        boundaries_text = []
        for boundary in boundaries_all:
            regex_region = re.compile(r'\b{}\b'.format(boundary), re.IGNORECASE)
            results = re.findall(regex_region, self.web_text)
            boundaries_text += results
        Counter_boundaries_text = Counter(boundaries_text)

        boundaries_text = pd.DataFrame.from_dict(Counter_boundaries_text, orient='index').reset_index().rename(columns={'index': 'name', 0: 'count'})
        boundaries_text = pd.merge(boundaries_text, lvl_boundaries, on='name', how='inner')
        boundaries_text = gpd.GeoDataFrame(boundaries_text, geometry='geom')

        setattr(administrative_boundaries, name, boundaries_text)
        
    def export(self):
        pass
    

    def test_fun(self, lvl_boundaries, name):
        boundaries_all = set(lvl_boundaries['name'])
        self.ls = []
        for boundary in boundaries_all:
            regex_region = re.compile(r"(\b\w+\b)(?:\W*)(?:\s*)(\b{}\b)".format(boundary), re.IGNORECASE)
            results = re.findall(regex_region, self.web_text)
            self.ls += results
            
            
        boundaries_text = gpd.GeoDataFrame(self.ls, columns=['prev_word', 'name'])
        boundaries_text = pd.merge(boundaries_text, lvl_boundaries, on='name', how='inner')
        boundaries_text.geometry = boundaries_text['geom']
        setattr(administrative_boundaries, name, boundaries_text)
        






        