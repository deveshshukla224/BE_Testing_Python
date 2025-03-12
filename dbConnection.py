import mysql.connector
import ssl
import json
from utilities import readfromglobalproperties


# Read credentials from a file
# with open('/home/devslane-75/Devesh/be_python_automation_testing/data_directory/database_creds.json') as f:
#     creds = json.load(f)
# username = creds['username']
# password = creds['password']

# username_value ="root"
# password_value ="Password@123"
# host_value ="localhost"
# database_value ="APIDevelop"

username_value = readfromglobalproperties.read_config_from_global_properties("SQL","username")
password_value = readfromglobalproperties.read_config_from_global_properties("SQL","password")
host_value = readfromglobalproperties.read_config_from_global_properties("SQL","host")
database_value = readfromglobalproperties.read_config_from_global_properties("SQL","database")

# if username_value_from_global_properties==username_value:
#     print("username is same")
    
# else:
#     print("username is different")
#     print("username_value_from_global_properties",username_value_from_global_properties)
#     print("username_value",username_value)
    
    
# print("username_value",type(username_value))
# print("localhost type",type("localhost"))
# print("password_value",password_value)
# print("host_value",host_value)
# print("database_value",database_value)
#create connection from python to db
# Create a connection
conn = mysql.connector.connect(
    host=host_value,
    user=username_value,
    password=password_value,
    database=database_value,
    ssl_disabled=True
)


#check if connection is established
print("connection with python and db is established",conn.is_connected())
#create cursor object to execute queries and fetch results
cursor = conn.cursor()
# Show Tables
cursor.execute("select * from CustomerInfo") 

#Fetch all results
rows = cursor.fetchall()

# Print results
for row in rows:
    print(row)

##############

# row_one_only = cursor.fetchone()  # Fetch only the first row
# print(row_one_only)


# row = cursor.fetchone()
# print(row)

# Close connection
cursor.close()
conn.close()