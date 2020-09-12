# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:53:41 2020

@author: acer
"""
import yaml
from datetime import datetime
file = open("Matches from 2015 to 2020.txt", "r+")
file_lines=file.readlines()
start_year=2015
end_year=2015
output_filename='Matches from {a} to {b}.txt'.format(a=start_year, b=end_year)
for file_number in range(len(file_lines)):
    match_name=file_lines[file_number]
    match_name.replace("\n", '')
    
    with open(r'C:\Users\acer\Desktop\Bhanvaanu\DL\Match Data\%s.yaml'%match_name[:-6]) as file:
        match = yaml.load(file, Loader=yaml.FullLoader)
    date=match.get('info').get('dates')
    if(type(date[0])!=str):
        match_year=date[0].strftime('%Y')
        match_year=int(match_year)
    else:
        match_date=date[0]
        match_year=int(match_date[:4])
    
    if(match.get('info').get('gender')=='male'):
        if(match_year<=end_year and match_year>=start_year):
            print(file_lines[file_number], file=open(output_filename, 'a'),end='')
    print('{a}%'.format(a=100*file_number/len(file_lines)))