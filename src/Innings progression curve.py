# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 20:17:28 2020

@author: Swar Vaidya
"""


import yaml
import matplotlib.pyplot as plt 

total_runs1_0_10 = 0
total_runs1_10_20 = 0
total_runs1_20_30 = 0
total_runs1_30_40 = 0
total_runs1_40_50 = 0
    
total_balls1_0_10 = 0
total_balls1_10_20 = 0
total_balls1_20_30 = 0
total_balls1_30_40 = 0
total_balls1_40_50 = 0

avg_runrate1=[0,0,0,0,0]


total_runs2_0_10 = 0
total_runs2_10_20 = 0
total_runs2_20_30 = 0
total_runs2_30_40 = 0
total_runs2_40_50 = 0
    
total_balls2_0_10 = 0
total_balls2_10_20 = 0
total_balls2_20_30 = 0
total_balls2_30_40 = 0
total_balls2_40_50 = 0

avg_runrate2=[0,0,0,0,0]
first_runs=[]
second_runs=[]





file = open("Matches from 2015 to 2015.txt", "r+")
file_lines=file.readlines()

total_runrate1=[0,0,0,0,0]
for file_number in range(len(file_lines)):
    match_name=file_lines[file_number]
    match_name.replace("\n", '')
    
    
    
    with open(r'C:\Users\acer\Desktop\Bhanvaanu\DL\Match Data\%s.yaml'%match_name[:-6]) as file:
        match = yaml.load(file, Loader=yaml.FullLoader)
    innings=match.get('innings')
    innings_1 = innings[0].get('1st innings').get('deliveries')
    innings_2 = innings[1].get('2nd innings').get('deliveries')
    
    
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
    #Second Innings:    
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
    first_runs.append(total_runs)
    second_runs.append(total_runs_2)
    
    '''
    #Plot
    from datetime import datetime
    from team_color import TeamColor
    team_1_color=TeamColor(innings[0].get('1st innings').get('team'))
    team_2_color=TeamColor(innings[1].get('2nd innings').get('team'))
    plt.plot(runs, color=team_1_color, linewidth = 1, markevery=markers_1, marker='s')
    plt.plot(runs_2, color=team_2_color, linewidth = 1, markevery=markers_2, marker='s')
    plt.xlabel('Balls')
    plt.ylabel('Runs')
    teams=['{a} {b}'.format(a=innings[0].get('1st innings').get('team'), b=score_1) ,'{a} {b}'.format(a= innings[1].get('2nd innings').get('team'), b=score_2)]
    plt.legend(teams) 
    plt.grid('major')
    date=match.get('info').get('dates')
    if(type(date[0])!=str):
        date=date[0].strftime('%d/%m/%Y')
    else:
        date=date[0]
    venue=match.get('info').get('city')
    if(venue==None): venue= match.get('info').get('venue')
    title='{a} VS {b} ({c}, {d})'.format(a=match.get('info').get('teams')[0],b=match.get('info').get('teams')[1], c=venue, d=date)
    
    plt.title(title)
    #plt.savefig('{a}.png'.format(a=title), format='png')
    
    '''
    
    
    
    #Piece wise run-rate calculation
    
    

        
    balls=len(runs)-1
    if(len(runs)>60):
        runs1_0_10 = (runs[60]-runs[0])
        balls1_0_10 = 60
        if(len(runs)>120):
            runs1_10_20 = (runs[120]-runs[60])
            balls1_10_20 = 60
            if(len(runs)>180):
                runs1_20_30 = (runs[180]-runs[120])
                balls1_20_30 = 60
                if(len(runs)>240):
                    runs1_30_40 = (runs[240]-runs[180])
                    balls1_30_40 = 60
                    if(len(runs)==301):
                        runs1_40_50 = (runs[300]-runs[240])
                        balls1_40_50=60
                    else:
                        runs1_40_50 = (runs[balls]-runs[240])
                        balls1_40_50 = balls-240
                else:
                    runs1_30_40 = (runs[balls]-runs[180])
                    balls1_30_40 = balls-180
            else:
                runs1_20_30 = (runs[balls]-runs[120])
                balls1_20_30 = balls-120
        else:
            runs1_10_20 = (runs[balls]-runs[60])
            balls1_10_20 = balls-60
    else:
        runs1_0_10 = (runs[balls])
        balls1_0_10 = balls
                    
                                
    total_runs1_0_10 = total_runs1_0_10 + runs1_0_10
    total_runs1_10_20 = total_runs1_10_20 + runs1_10_20
    total_runs1_20_30 = total_runs1_20_30 + runs1_20_30
    total_runs1_30_40 = total_runs1_30_40 + runs1_30_40
    total_runs1_40_50 = total_runs1_40_50 + runs1_40_50
    
    total_balls1_0_10 = total_balls1_0_10 + balls1_0_10
    total_balls1_10_20 = total_balls1_10_20 + balls1_10_20
    total_balls1_20_30 = total_balls1_20_30 + balls1_20_30
    total_balls1_30_40 = total_balls1_30_40 + balls1_30_40
    total_balls1_40_50 = total_balls1_40_50 + balls1_40_50
    
    
    
    
    balls_2=len(runs_2)-1
    if(len(runs_2)>60):
        runs2_0_10 = (runs_2[60]-runs_2[0])
        balls2_0_10 = 60
        if(len(runs_2)>120):
            runs2_10_20 = (runs_2[120]-runs_2[60])
            balls2_10_20 = 60
            if(len(runs_2)>180):
                runs2_20_30 = (runs_2[180]-runs_2[120])
                balls2_20_30 = 60
                if(len(runs_2)>240):
                    runs2_30_40 = (runs_2[240]-runs_2[180])
                    balls2_30_40 = 60
                    if(len(runs_2)==301):
                        runs2_40_50 = (runs_2[300]-runs_2[240])
                        balls2_40_50=60
                    else:
                        runs2_40_50 = (runs_2[balls_2]-runs_2[240])
                        balls2_40_50 = balls_2-240
                else:
                    runs2_30_40 = (runs_2[balls_2]-runs_2[180])
                    balls2_30_40 = balls_2-180
            else:
                runs2_20_30 = (runs_2[balls_2]-runs_2[120])
                balls2_20_30 = balls_2-120
        else:
            runs2_10_20 = (runs_2[balls_2]-runs_2[60])
            balls2_10_20 = balls_2-60
    else:
        runs2_0_10 = (runs_2[balls_2])
        balls2_0_10 = balls_2
                    
                                
    total_runs2_0_10 = total_runs2_0_10 + runs2_0_10
    total_runs2_10_20 = total_runs2_10_20 + runs2_10_20
    total_runs2_20_30 = total_runs2_20_30 + runs2_20_30
    total_runs2_30_40 = total_runs2_30_40 + runs2_30_40
    total_runs2_40_50 = total_runs2_40_50 + runs2_40_50
    
    total_balls2_0_10 = total_balls2_0_10 + balls2_0_10
    total_balls2_10_20 = total_balls2_10_20 + balls2_10_20
    total_balls2_20_30 = total_balls2_20_30 + balls2_20_30
    total_balls2_30_40 = total_balls2_30_40 + balls2_30_40
    total_balls2_40_50 = total_balls2_40_50 + balls2_40_50


avg_runrate1[0]= 6*total_runs1_0_10/total_balls1_0_10
avg_runrate1[1]= 6*total_runs1_10_20/total_balls1_10_20
avg_runrate1[2]= 6*total_runs1_20_30/total_balls1_20_30
avg_runrate1[3]= 6*total_runs1_30_40/total_balls1_30_40
avg_runrate1[4]= 6*total_runs1_40_50/total_balls1_40_50
    
avg_runrate2[0]= 6*total_runs2_0_10/total_balls2_0_10
avg_runrate2[1]= 6*total_runs2_10_20/total_balls2_10_20
avg_runrate2[2]= 6*total_runs2_20_30/total_balls2_20_30
avg_runrate2[3]= 6*total_runs2_30_40/total_balls2_30_40
avg_runrate2[4]= 6*total_runs2_40_50/total_balls2_40_50

print(avg_runrate1)
print(avg_runrate2)




#avg_runrate1=[4.435, 4.433, 4.65, 5.22, 7.40]
#avg_runrate2=[4.82, 4.63, 4.85, 5.2, 6.33]
'''average_run_progression1=[]
cumm_average_run_progression1=[]
for i in range(5):
    for j in range(10):
        average_run_progression1.append(avg_runrate1[i])
        
for i in range(50):
    cumm_average_run_progression1.append((sum(average_run_progression1[:i+1])))
   
average_run_progression2=[]
cumm_average_run_progression2=[]
for i in range(5):
    for j in range(10):
        average_run_progression2.append(avg_runrate2[i])
        
for i in range(50):
    cumm_average_run_progression2.append((sum(average_run_progression2[:i+1])))
plt.clf()  
percent_avg_run_prog1=[0]
percent_avg_run_prog2=[0]
for i in range(50):
    percent_avg_run_prog1.append (100*cumm_average_run_progression1[i]/cumm_average_run_progression1[49])
    percent_avg_run_prog2.append (100*cumm_average_run_progression2[i]/cumm_average_run_progression2[49])

x_axis=[]
for i in range(51): 
    x_axis.append(i)
   
plt.plot(x_axis, percent_avg_run_prog1)
plt.plot(x_axis, percent_avg_run_prog2)  
plt.xlabel('Overs')
plt.ylabel('Percentage of Total Runs')  
plt.title('Innings Progression Comparision')
legend=['First Innings', 'Second Innings']
plt.legend(legend)
plt.grid()
import os'''
#os.chdir(r'C:\Users\acer\Desktop\Bhanvaanu\DL')
#plt.savefig('% Innings progression 2019.pdf', format='pdf')



#Average Runs:
from statistics import mean
import numpy as np
G50_1 = mean(first_runs)
G50_2 = mean(second_runs)
G50 = ( (len(first_runs)*G50_1)  +  (len(second_runs)*G50_2) )/( len(first_runs) + len(second_runs) )
median_1 = np.median(first_runs)
median_2=np.median(second_runs)
median_odi = np.median(first_runs + second_runs)
print('First Innings Average Score : {a} Runs'.format(a=round(G50_1)))
print('Second Innings Average : {b} Runs'.format(b=round(G50_2)))
print('Odi Average Score : {c} Runs'.format(c=round(G50)))
print('First Innings Median Score : {a} Runs'.format(a=median_1))
print('Second Innings Median Score : {b} Runs'.format(b=median_2))
print('ODI Median Score : {c} Runs'.format(c=median_odi))


#Histogram

hist_bin=[]
for i in range(500):
    hist_bin.append(1*(i+1))
plt.clf()
plt.hist(first_runs, bins= hist_bin, color='blue')   
plt.grid()
plt.xlabel('Runs')
plt.ylabel('Frequency')
plt.title('Frequency of Runs Scored in ODIs')
import os
os.chdir(r'C:\Users\acer\Desktop\Bhanvaanu\DL')
plt.savefig('Frequency of Runs (2015).pdf', format='pdf')



#export to CSV
'''import csv
csv_filename='First Innings data.csv'
with open(csv_filename, 'w', newline='') as csvfile:  
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(runs) 
    csvwriter.writerow(runs_2)'''





