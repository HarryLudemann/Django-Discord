# This file Controls Config Functions (Create, Get, Set)
from configparser import ConfigParser

# Create Config File
def CreateConfigFile(GuildID, UserID):
    #Get the configparser object
    config_object = ConfigParser()

    # parse existing file
    config_object.read('config.ini')

    # add a new section and some values
    config_object.add_section(GuildID)
    config_object.set(GuildID, 'userid', UserID)
    config_object.set(GuildID, 'identifier', '$')
    config_object.set(GuildID, 'fun-inspire', '@everyone')
    config_object.set(GuildID, 'fun-comeback', '@everyone')
    config_object.set(GuildID, 'fun-cat', '@everyone')
    config_object.set(GuildID, 'fun-dog', '@everyone')
    config_object.set(GuildID, 'fun-fox', '@everyone')
    config_object.set(GuildID, 'basic-ping', '@everyone')
    config_object.set(GuildID, 'admin-quit', 'Admin')
    config_object.set(GuildID, 'admin-changeprefix', 'Admin')
    config_object.set(GuildID, 'admin-test', 'Admin')

    #Write the above sections to config.ini file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

# Get Saved Config Value
def GetConfigValue(Value, GuildID):
    #Read config.ini file
    config_object = ConfigParser()
    config_object.read("config.ini")
    #Create Object Of ServerSettings
    ServerSettings = config_object[GuildID]
    return ServerSettings[Value]

# Set Config Value to file
def SetConfigValue(Value, NewValue, GuildID):
    config_object = ConfigParser()
    config_object.read("config.ini")
    #Create Object Of ServerSettings
    ServerSettings = config_object[GuildID]
    #Update the value
    ServerSettings[Value] = NewValue
    #Write changes back to file
    with open('config.ini', 'w') as conf:
        config_object.write(conf)

if (__name__ == "__main__"):
    CreateConfigFile('677326100686438430') # GuildID For HAX00R
