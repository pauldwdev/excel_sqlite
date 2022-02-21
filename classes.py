# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:50:54 2022

@author: paul
"""


class populationRecord:
    
    tableName = 'population'
    
    def __init__(self, date, cocroachCount):
        self.date = date
        self.cocroachCount = cocroachCount
            
    def createInsert(self):
        return 'insert into ' + self.tableName + ' (date, cocroach_count) values ( \'' + str(self.date) + '\',' + str(self.cocroachCount) + ');'
    
        
class foodRecord:
    
    tableName = 'food'
    
    def __init__(self, date, food):
        self.date = date
        self.food = food
        
    def createInsert(self):
        return 'insert into ' + self.tableName + ' (date, food) values ( \'' + str(self.date) + '\',' + str(self.food) + ');'
    
      