# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 11:05:49 2020

@author: acer
"""

def TeamColor(team):
    #International Teams
    if(team=='India'): color='#1E90FF'
    elif(team=='Pakistan'): color='#00FF00'
    elif(team=='Bangladesh'): color='#006400'
    elif(team=='Sri Lanka'): color='#00008B'
    elif(team=='Australia'): color='#FFFF00'
    elif(team=='England'): color='#0000FF'
    elif(team=='New Zealand'): color='#000000'
    elif(team=='West Indies'): color='#800000'
    elif(team=='South Africa'): color='#ADFF2F'
    elif(team=='Ireland'): color='#86EF76'
    elif(team=='Afghanistan'): color='#FF0000'
    elif(team=='Bermuda'): color='#0000FF'
    elif(team=='Zimbabwe'): color='#DC143C'
    elif(team=='UAE'): color='#A9A9A9'
    elif(team=='Netherlands'): color='#FF8C00'
    elif(team=='Canada'): color='#FF0000'
    elif(team=='Scotland'): color='#0000CD'
    
    
    
    #IPL Teams
    elif(team=='Royal Challengers Bangalore'): color='#FF0000'
    elif(team=='Sunrisers Hyderabad'): color='#FFA500'
    elif(team=='Deccan Chargers'): color='#483D8B'
    elif(team=='Kings XI Punjab'): color='#C0C0C0'
    elif(team=='Chennai Super Kings'): color='#FFFF00'
    elif(team=='Gujarat Lions'): color='#FF8C00'
    elif(team=='Mumbai Indians'): color='#1E90FF'
    elif(team=='Delhi Daredevils'): color='#191970'
    elif(team=='Delhi Capitals'): color='#0000FF'
    elif(team=='Rajasthan Royals'): color='#00008B'
    elif(team=='Kochi Tuskers Kerala'): color='#FF8C00'
    elif(team=='Rising Pune Supergiants'): color='#800080'
    elif(team=='Pune Warriors'): color='#00BFFF'
    elif(team=='Kolkata Knight Riders'): color='#4B0082'
    
    
    else: color=None
    return color
