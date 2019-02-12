# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:04:06 2019

@author: David Röbl
"""

import geopandas as gpd
import psycopg2


class PostgresConnection():
    
    def __init__(self, host: str, database: str, user: str, password: str):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
    
    def connect(self):
        try:
            self.conn = psycopg2.connect(host=self.host, database=self.database, user=self.user, password=self.password)
            print('Connection succesfull')
        except:
            print('Unable to connect with database')


class AdminBoundaries(PostgresConnection):

    def __init__(self, host: str, database: str, user: str, password: str):
        super().__init__(host, database, user, password)
    
    def load_austrian_boundaries(self):
        sql_statement = '''SELECT kg as kastralgemeinde,
                        pg as gemeinde, 
                        pb as bezirk, 
                        bl as bundesland, 
                        st as land, 
                        geom 
                        FROM oe_verwaltungsgrenzen;'''
        
        self.kastralgemeinden = gpd.GeoDataFrame.from_postgis(sql_statement, self.conn).rename(columns={'kastralgemeinde': 'name'})
        self.gemeinden = self.kastralgemeinden.dissolve(by='gemeinde').loc[:, ['bezirk', 'bundesland', 'land', 'geom']].reset_index().rename(columns={'gemeinde': 'name'})
        self.bezirke = self.kastralgemeinden.dissolve(by='bezirk').loc[:, ['bundesland', 'land', 'geom']].reset_index().rename(columns={'bezirk': 'name'}) 
        self.bundesländer = self.kastralgemeinden.dissolve(by='bundesland').loc[:, ['land', 'geom']].reset_index().rename(columns={'bundesland': 'name'})
    
    
    def load_nuts_boundaries(self):
        pass
    

class OsmData():

    def __init__(self):
        pass
    
    
class GeoNames():
    
    def __init__(self):
        pass
    

# Österreich = AdminBoundaries('localhost', 'GES_Data', 'postgres', '072278895') 
# Österreich.connect()
# Österreich.load_austrian_boundaries()


    
    
