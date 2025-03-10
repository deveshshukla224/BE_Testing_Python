from configparser import ConfigParser

def read_config_from_global_properties(section, key):
    config = ConfigParser()
    #read from the file
    config.read('/home/devslane-75/Devesh/be_python_automation_testing/configuations/global_properties.ini')
    #return the value of the key from a section
    return config.get(section, key)

#usage
#print(read_config_from_global_properties('API', 'URL'))