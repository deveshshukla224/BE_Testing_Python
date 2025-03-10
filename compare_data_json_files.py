import json

#open and parse data of file 1

with open("/home/devslane-75/Devesh/be_python_automation_testing/data_directory/data.json",'r') as file1:
    data1 = json.load(file1)
    
with open("/home/devslane-75/Devesh/be_python_automation_testing/data_directory/data2.json",'r') as file2:
    data2 = json.load(file2)
   
   
#load data from file 1 and file 2 and compare them 
if data1 == data2:
    print("Data is same")
else:
    print("Data is different")