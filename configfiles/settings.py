import yaml

class GlobalVars():

    def fetchVar(self,arg):
        stream = open('E:\Python-SeleniumFramework\PythonFramework\configfiles\Params.YML', 'r')
        data = yaml.load(stream)
        return data[arg]

