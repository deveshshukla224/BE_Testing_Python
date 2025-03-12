from readfromglobalproperties import getQuery
#class to store the resources
# class APIResources:
class APIResources:
    users='api/users'
    login = '/api/login'
    

def buildPayloadFromDBData(query):
    data_body= {}
    received_data_from_db = getQuery(query)
    data_body['username'] = received_data_from_db[0]
    data_body['password'] = received_data_from_db[1]
    return data_body