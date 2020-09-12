import yaml, os, csv

data_path = os.getcwd()+'/../data/odis/'
list_path = data_path+'../list/odis_list.yaml'

list_obj = open(list_path)
match_list = yaml.load(list_obj, Loader=yaml.FullLoader)

for match_number in match_list:
    match_obj = open(data_path+match_number)
    match = yaml.load(match_obj, Loader=yaml.FullLoader)

    innings_1 = match.get('innings')[0].get('1st innings').get('deliveries')
    innings_2 = match.get('innings')[1].get('2nd innings').get('deliveries')

    runs_1, wicket_1 = [], []
    ext_run,ext_wicket = 0, 0

    for i in innings_1:
        ball_dict=list(i.keys())[0]

        ball_run = i.get(ball_dict).get('runs').get('total')
        ball_wicket = 0 if i.get(ball_dict).get('wicket')==None else 1

        if (i.get(ball_dict).get('extras')!=None) and (i.get(ball_dict).get('extras').get('noballs')!=None or i.get(ball_dict).get('extras').get('wides')!=None):
            ext_run = ext_run + ball_run
            ext_wicket = ext_wicket + ball_wicket
        else:
            if len(runs_1)==0:
                ball_run, ball_wicket = ball_run+ext_run, ball_wicket+ext_wicket
                runs_1.append(ball_run)
                wicket_1.append(ball_wicket)
                ext_run,ext_wicket = 0, 0
            else:
                ball_run, ball_wicket = runs_1[-1]+ball_run+ext_run, wicket_1[-1]+ball_wicket+ext_wicket
                runs_1.append(ball_run)
                wicket_1.append(ball_wicket)
                ext_run,ext_wicket = 0, 0

    runs_2, wicket_2 = [], []
    ext_run,ext_wicket = 0, 0

    for i in innings_2:
        ball_dict=list(i.keys())[0]

        ball_run = i.get(ball_dict).get('runs').get('total')
        ball_wicket = 0 if i.get(ball_dict).get('wicket')==None else 1

        if (i.get(ball_dict).get('extras')!=None) and (i.get(ball_dict).get('extras').get('noballs')!=None or i.get(ball_dict).get('extras').get('wides')!=None):
            ext_run = ext_run + ball_run
            ext_wicket = ext_wicket + ball_wicket
        else:
            if len(runs_2)==0:
                ball_run, ball_wicket = ball_run+ext_run, ball_wicket+ext_wicket
                runs_2.append(ball_run)
                wicket_2.append(ball_wicket)
                ext_run,ext_wicket = 0, 0
            else:
                ball_run, ball_wicket = runs_2[-1]+ball_run+ext_run, wicket_2[-1]+ball_wicket+ext_wicket
                runs_2.append(ball_run)
                wicket_2.append(ball_wicket)
                ext_run,ext_wicket = 0, 0

    data = [runs_1, wicket_1, runs_2, wicket_2]
    with open(data_path+'../csv_raw/odis/'+match_number.split('.')[0]+'.csv',"w+") as my_csv:
        csvWriter = csv.writer(my_csv,delimiter=',')
        csvWriter.writerows(data)