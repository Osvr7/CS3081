from logic import *

rain = Symbol("rain") # It's raining 
hagrid = Symbol("hagrid") # Harry visit Hagrid
dumbledore = Symbol("dumbledore") # Harry visit Dumbledore

sentence = And(rain, hagrid)

print(sentence.formula())

#knowledge = Implication(Not(rain), hagrid)
knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore)

print(knowledge.formula())