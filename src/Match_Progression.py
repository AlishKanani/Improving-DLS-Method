# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:17:28 2020

@author: Swar Vaidya
"""


import yaml
import matplotlib.pyplot as plt 
from os import listdir
from os.path import isfile, join
mypath= r'C:\Users\acer\Desktop\Bhanvaanu\DL\Ipl Data'
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for file_number in range(len(onlyfiles)):
    with open(r'C:\Users\acer\Desktop\Bhanvaanu\DL\Ipl Data\{filename}'.format(filename=onlyfiles[file_number])) as file:
        match = yaml.load(file, Loader=yaml.FullLoader)
    innings=match.get('innings')
    innings_1 = innings[0].get('1st innings').get('deliveries')
    if(len(innings)>=2):
        innings_2 = innings[1].get('2nd innings').get('deliveries')
    else:
        innings_2=[]
    
    
    #First Innings:
    innings_1_balls=[]
    runs_by_ball=[0]
    runs=[0]
    markers_1=[]
    ball_number=0
    for i in range(len(innings_1)):
        
        innings_1_balls.append(innings_1[i])
        ball_run=innings_1[i].get(list(innings_1[i].keys())[0]).get('runs').get('total')
        
        if(innings_1[i].get(list(innings_1[i].keys())[0]).get('extras')!=None):
            if(innings_1[i].get(list(innings_1[i].keys())[0]).get('extras').get('noballs') != None or innings_1[i].get(list(innings_1[i].keys())[0]).get('extras').get('wides')!= None):
                runs_by_ball[len(runs_by_ball)-1]=runs_by_ball[len(runs_by_ball)-1]+ball_run
            else:
                ball_number=ball_number+1
                runs_by_ball.append(int(ball_run))
                runs.append(sum(runs_by_ball))  
            
        else:
            ball_number=ball_number+1
            runs_by_ball.append(int(ball_run))
            runs.append(sum(runs_by_ball))  
            
        
        if(innings_1[i].get(list(innings_1[i].keys())[0]).get('wicket') != None):
            markers_1.append(ball_number)
            
    total_runs=runs[len(runs)-1]
    wickets_1 = len(markers_1)
    full_overs_1=int(ball_number/6)
    current_over_balls_1= ball_number - (full_overs_1*6)
    overs_1='{a}.{b}'.format(a=full_overs_1, b=current_over_balls_1)
    score_1='{a}/{b} ({c} overs)'.format(a=total_runs, b=wickets_1, c=overs_1)
    
    #Second Inninga:    
    innings_2_balls=[]
    runs_by_ball_2=[0]
    runs_2=[0]
    markers_2=[]
    ball_number_2=0
    for i in range(len(innings_2)):
        innings_2_balls.append(innings_2[i])
        ball_run=innings_2[i].get(list(innings_2[i].keys())[0]).get('runs').get('total')
        
        if(innings_2[i].get(list(innings_2[i].keys())[0]).get('extras')!=None):
            if(innings_2[i].get(list(innings_2[i].keys())[0]).get('extras').get('noballs') != None or innings_2[i].get(list(innings_2[i].keys())[0]).get('extras').get('wides')!= None):
                runs_by_ball_2[len(runs_by_ball_2)-1]=runs_by_ball_2[len(runs_by_ball_2)-1]+ball_run
            else:
                ball_number_2=ball_number_2+1
                runs_by_ball_2.append(int(ball_run))
                runs_2.append(sum(runs_by_ball_2)) 
        else:
            ball_number_2=ball_number_2+1
            runs_by_ball_2.append(int(ball_run))
            runs_2.append(sum(runs_by_ball_2))  
    
        if(innings_2[i].get(list(innings_2[i].keys())[0]).get('wicket') != None):
            markers_2.append(ball_number_2)
    total_runs_2=runs_2[len(runs_2)-1]
    wickets_2=len(markers_2)
    full_overs_2=int(ball_number_2/6)
    current_over_balls_2= ball_number_2 - (full_overs_2*6)
    overs_2='{a}.{b}'.format(a=full_overs_2, b=current_over_balls_2)
    score_2='{a}/{b} ({c} overs)'.format(a=total_runs_2, b=wickets_2, c=overs_2)
    
    
    
    from datetime import datetime
    from team_color import TeamColor
    team_1_color=TeamColor(innings[0].get('1st innings').get('team'))
    if(len(innings)>=2):
        team_2_color=TeamColor(innings[1].get('2nd innings').get('team'))
    else:
        team_2_color=None
    plt.plot(runs, color=team_1_color, linewidth = 1, markevery=markers_1, marker='s')
    plt.plot(runs_2, color=team_2_color, linewidth = 1, markevery=markers_2, marker='s')
    plt.xlabel('Balls')
    plt.ylabel('Runs')
    if(len(innings)>=2):
        teams=['{a} : {b}'.format(a=innings[0].get('1st innings').get('team'), b=score_1) ,'{a} : {b}'.format(a= innings[1].get('2nd innings').get('team'), b=score_2)]
    else:
        teams=['{a} : {b}'.format(a=innings[0].get('1st innings').get('team'), b=score_1)]
    plt.legend(teams) 
    plt.grid('major')
    
    date=match.get('info').get('dates')
    if(type(date[0])!=str):
        match_date=date[0].strftime('%d/%m/%Y')
    else:
        match_date=date[0]
    venue=match.get('info').get('city')
    if(match.get('info').get('outcome').get('winner') != None):
        winner=match.get('info').get('outcome').get('winner')
        win_by=match.get('info').get('outcome').get('by')
        if(win_by.get('wickets')!=None):
            if(match.get('info').get('outcome').get('method') != None):
                result=('{winner} won by {wickets} wickets ({Dl} method)'.format(winner=winner, wickets=win_by.get('wickets'), Dl=match.get('info').get('outcome').get('method')))
            else:
                result=('{winner} won by {wickets} wickets'.format(winner=winner, wickets=win_by.get('wickets'), Dl=match.get('info').get('outcome').get('method')))

        elif(win_by.get('runs')!=None):
            if(match.get('info').get('outcome').get('method') != None):
                result=('{a} won by {b} runs ({Dl} method)'.format(a=winner, b=win_by.get('runs'), Dl=match.get('info').get('outcome').get('method')))
            else:
                result=('{a} won by {b} runs'.format(a=winner, b=win_by.get('runs')))
    elif(match.get('info').get('outcome').get('result')!=None):
        result=('{a}'.format(a=match.get('info').get('outcome').get('result')))
    else:
        result='No idea boss'
        print(onlyfiles[file_number])

    if(venue==None): venue= match.get('info').get('venue')
    title='{a} VS {b} ({c}, {d}) \n {e}'.format(a=match.get('info').get('teams')[0],b=match.get('info').get('teams')[1], c=venue, d=match_date, e=result)
    
    plt.title(title)
    import os
    os.chdir(r"C:\Users\acer\Desktop\Bhanvaanu\DL\IPL graphs")
    #plt.savefig('{a}.png'.format(a=title), format='png')
    
    if(type(date[0])!=str):
        file_date=date[0].strftime('%Y-%m-%d')
    else:
        file_date=date[0]
    output_filename='({date}) {a} VS {b} ({c})'.format(date=file_date, a=match.get('info').get('teams')[0],b=match.get('info').get('teams')[1], c=onlyfiles[file_number])
    plt.savefig('{a}.png'.format(a=output_filename), format='png')
    plt.clf()    
