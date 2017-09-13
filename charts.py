#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 15:10:59 2017

@author: dxy
"""

import csv

def loadRegionData():
    regions = {}
    with open('gapminder_regions.csv') as csvfile:
        regionReader = csv.DictReader(csvfile)
        for row in regionReader:
            regions[row['Country']] = row ['Group']
    return regions


def loadChartData():
    ages = []
    with open('Indicator_Average_age.csv') as csvfile:
        ageReader = csv.DictReader(csvfile)
        for row in ageReader:
            ages.append([row['Average age of billionaires'], float(row['2004']),
                         float(row['2005']), float(row['2006']), float(row['2007'])])
    return ages

def scatterData(ages, regions):
    mapRegion = {'East Asia & Pacific': 1, 'Sub-Saharan Africa': 2, 'Middle East & North Africa': 3,
                 'South Asia': 4, 'America': 5, 'Europe & Central Asia': 6}
    x = []
    y = []
    radius = []
    for age in ages:
        if age[-1]:
            tmp = regions.get(age[0])
            if tmp:
                x.append(mapRegion.get(tmp))
                y.append(age[-1])
                radius.append(age[-1]/1000)

    return x,y,radius

# ages = loadChartData()
def lineData(ages):
    line = {}
    for age in ages:
        if age[-1]:
            line[age[0]] = age[1:]

    return line








