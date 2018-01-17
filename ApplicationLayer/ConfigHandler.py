import ConfigParser
Config = ConfigParser.ConfigParser()
Config.read("config.ini")

class ConfigHandler():
    def ConfigSectionMap(section):
        dict1 = {}
        options = Config.options(section)
        for option in options:
            try:
                dict1[option] = Config.get(section, option)
                if dict1[option] == -1:
                   print 'dict1 is -1'
            except:
                print("exception on %s!" % option)
                dict1[option] = None
        return dict1

    pathvariable = ConfigSectionMap("Database")['databasepath']



