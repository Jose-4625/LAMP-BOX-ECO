import json
sim = {
    "subRoutine":{
        "idx": 1,
        "minTemp":[23,23,23],
        "maxTemp":[23,34,45],
        "dur":[30,30,30],
        "cycle": False
    }
}
simJSON = '{"subRoutine":{"idx":"1","minTemp":[453,554],"maxTemp":[453,554],"dur":[4545,54],"cycle":["cycleOn","cycleOn"]}}'#json.dumps(sim)
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
       _._subRoutines.append(_)
       return _
   _subRoutines = []
   def __init__(self,jsonSTR):
       idx,temp,dur,cycle = jsonPyObjCov(jsonSTR)
       self.idx = idx
       self.temp_dur = list(zip(temp,dur))
       self.cycle = cycle
   def show(self):
       print(Routine._subRoutines)
   def __repr__(self):
       return str(self.__dict__)




if __name__ == "__main__":
    vir = Routine.addSubRoutine(simJSON)
    vir.show()
