try:
    import json
except:
    import ujson as json
sim = {
    "subRoutine":{
        "idx": 1,
        "minTemp":[23,23,23],
        "maxTemp":[23,34,45],
        "dur":[30,30,30],
        "cycle": False
    }
}
simJSON = '{"subRoutine":{"idx":"1","minTemp":[453,554],"maxTemp":[453,554],"dur":[4545,54],"cycle":[40,30]}}'#json.dumps(sim)
#print(simJSON)
"====================================Simulated JSON dump============================================="
"""JSON to Python interface """
def jsonPyObjCov(jsonSTR):
    pyObj = json.loads(jsonSTR)
    #print(pyObj)
    return pyObj["subRoutine"]['idx'], pyObj["subRoutine"]['maxTemp'],pyObj["subRoutine"]['dur'],pyObj["subRoutine"]['cycle']

""""Data model"""
class Routine(object):

   @classmethod
   def addSubRoutine(cls, jsonStr):
       _ = cls(jsonStr)
       del _._subRoutines[:]
       _._subRoutines.append(_)
       return _
   _subRoutines = []
   def __init__(self,jsonSTR):
       idx,temp,dur,cycle = jsonPyObjCov(jsonSTR)
       self.idx = idx
       self.temp_dur = list(zip(temp,dur))
       self.cycle = cycle
   @classmethod
   def show(cls):
       print(Routine._subRoutines)
   def __repr__(self):
       return str(self.__dict__)




def test():
    vir = Routine.addSubRoutine(simJSON)
