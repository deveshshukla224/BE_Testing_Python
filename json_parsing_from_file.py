import json

#json in file
#json.load - returns python dictionary and take file as input
with open("/home/devslane-75/Devesh/be_python_automation_testing/data_directory/data.json",'r') as file:
    parsed_data=json.load(file)
    company_data = parsed_data['company']
    for key in company_data:
        if key=="employees":
            for i in company_data[key]:
                if i['name']=="Bob Smith":
                    print(i["position"])
            