# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:10:07 2019

@author: David Röbl
"""

import geopandas as gpd
import re


class SearchAdminBoundaries():

    def __init__(self, text: str):
        self.text = text

    def search_boundaries(self, boundary_gazetter: gpd.GeoDataFrame, attribute_name: str):
        boundaries_all = set(boundary_gazetter['name'])
        self.ls = []
        for boundary in boundaries_all:
            regex_region = re.compile(r"(\b\w+\b)(?:\W*)(?:\s*)(\b{}\b)".format(boundary), re.IGNORECASE)
            results = re.findall(regex_region, self.web_text)
            self.ls += results

        boundaries_text = gpd.GeoDataFrame(self.ls, columns=['prev_word', 'name'])
        boundaries_text = gpd.merge(boundaries_text, boundary_gazetter, on='name', how='inner')
        boundaries_text.geometry = boundaries_text['geom']
        setattr(SearchAdminBoundaries, attribute_name, boundaries_text)


class ValidateAdminBoundaries():

    def __init__(self):
        pass


class ExportAdminBoundaries():

    def __init__(self):
        pass


