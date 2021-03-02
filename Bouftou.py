# coding:utf-8

import random  # random attack
import json #import the attacks dictionary 
from Bouftou_classes import * #There are the Bouftou classes in this file
from Bouftou_dict import * #There are the Bouftou attacks in this file


"""
Begin the program
"""

### Creation of the Bouftous

Bouftou1=Bouftou(1,1,1)

BouftouN1 = BouftouNoir(random.randint(2,5),4,4)
BouftouN1 = BouftouNoir(5,random.randint(3,6),5)
BouftouD = BouftouDore  (10,10,random.randint(5,20))

### Launch the attacks : BouftouDore is crazy

try:
    BouftouD.bang()
except AttributeError:
    print("This monster does not know this attack")

try:
    BouftouD.black_hole()
except AttributeError:
    print("This monster does not know the attack {}" .format("black_hole"))

try:
    BouftouD.gold_punch()
except AttributeError:
    print("This monster does not know this attack")

