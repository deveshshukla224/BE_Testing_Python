from configparser import ConfigParser
import mysql.connector
import ssl
from mysql.connector import Error

def read_config_from_global_properties(section, key):
    config = ConfigParser()
    #read from the file
    config.read('/home/devslane-75/Devesh/be_python_automation_testing/configuations/global_properties.ini')
    #return the value of the key from a section
    return config.get(section, key)

#usage
#print(read_config_from_global_properties('API', 'URL'))

db_config = {
    'host': read_config_from_global_properties('SQL', 'host'),
    'user': read_config_from_global_properties('SQL', 'username'),
    'password': read_config_from_global_properties('SQL', 'password'),
    'database': read_config_from_global_properties('SQL', 'database_test'),
    'ssl_disabled': True
}

def create_DB_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        if connection.is_connected():
            print("Connection established")
            return connection
    except Error as e:
        print(e)
        return None
    #by using ** we are unpacking the dictionary and passing the values to the connect method 
    # and by using ** we are explicitely mentioning that it is a dictionary
    #one good thing about connect method is it accepts the dictionary as well
    #pass the dictionary with the key value pairs
    
#Generic method to create connection and execute the query and return the result
def getQuery(query):
    #create the connection
    connection = create_DB_connection()
    #create the cursor object to execute the query
    cursor = connection.cursor()
    #execute the query
    cursor.execute(query)
    #fetch the result and return it back to the calling method
    return cursor.fetchone()