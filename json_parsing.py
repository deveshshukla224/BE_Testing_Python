import json

#json in string
data_in_json_string = '{"name":"devesh","age":20}'

#json.loads - returns python dictionary and take string as input

data_in_dictionary=json.loads(data_in_json_string)


print("name is",data_in_dictionary["name"])

