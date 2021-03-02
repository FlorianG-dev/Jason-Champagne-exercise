from Bouftou_dict import * #There are the Bouftou attacks in this file
print (Bdico)
"""
We create different Bouftou classes
"""
### We create a mother class -> Bouftou

class Bouftou:

    #Name of the specie is Bouftou
    name = "Bouftou"

    #All the Bouftou have 3 characteristics : PV, PA, MP
    def __init__(self, PV, PA, MP):
        self.PV = PV
        self.PA = PA
        self.PM = MP 


    #All the Bouftous share the same attack : bang
    def bang (self):           
            print ("attack bang")
            


###We create now the sub-classes

class BouftouNoir (Bouftou):
    
    #BouftouNoir can use the attack black_hole

    def black_hole(self):
        print ("attack black_hole")


##We add the attack to the attacks dictionary
if "black_hole" in Bdico.keys():
    Bdico["black_hole"].append("BouftouNoir")
else:
    Bdico["black_hole"] = ["BouftouNoir"]


###We create now the sub-classes

class BouftouDore (Bouftou):
    
    #BouftouDore can use the attack gold_punch

    def gold_punch(self):
        print ("attack gold_punch")

##We add the attack to the attacks dictionary
if "gold_punch" in Bdico.keys():
    Bdico["gold_punch"].append("BouftouDore")
else:   
    Bdico["gold_punch"] = ["BouftouDore"]


##We add the attack bang to the attacks dictionary
if "bang" in Bdico.keys():
    Bdico["bang"].append("Bouftou")
    for subclass in Bouftou.__subclasses__():
        Bdico["bang"].append(subclass.__name__)
else:
    Bdico["bang"] = ["Bouftou"]
    for cls in Bouftou.__subclasses__():
        Bdico["bang"].append(cls.__name__)

print(Bdico)