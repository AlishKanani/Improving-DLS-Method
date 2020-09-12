import yaml, os

data_path= os.getcwd()+'/../data/odis/'

files = [f for f in os.listdir(data_path) if f.endswith(".yaml")]
match_list=[]

for file_number in files:
    file_obj = open(data_path+file_number)
    match = yaml.load(file_obj, Loader=yaml.FullLoader)
    outcome = match.get('info').get('outcome')
    if ((outcome.get('method')==None) and (outcome.get('winner')!=None) and (match.get('info').get('gender')=='male')):
        match_list.append(file_number)
    file_obj.close()

with open(data_path+'../list/odis_list.yaml', 'w') as outfile:
    yaml.dump(match_list, outfile, default_flow_style=False)