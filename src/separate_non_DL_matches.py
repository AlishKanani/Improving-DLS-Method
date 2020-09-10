# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:17:28 2020

@author: Swar Vaidya
"""


import yaml
from os import listdir
from os.path import isfile, join
mypath= r'C:\Users\acer\Desktop\Bhanvaanu\DL\Match Data'
output_filename='Matches without use of DL method.txt'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file_number in range(len(onlyfiles)):
    with open(r'C:\Users\acer\Desktop\Bhanvaanu\DL\Match Data\{filename}'.format(filename=onlyfiles[file_number])) as file:
        match = yaml.load(file, Loader=yaml.FullLoader)
    if(match.get('info').get('outcome').get('method') == None):
        if(match.get('info').get('outcome').get('winner') != None):
            print(onlyfiles[file_number], file=open(output_filename, 'a'))
    