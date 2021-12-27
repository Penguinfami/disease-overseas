import random
asia = 1
antartica = 2
northamerica = 3
europe = 4
oceania = 5
africa = 6
southamerica = 7

asiaC = False
antarticaC = False
northamericaC = False
europeC = False
oceaniaC = False
africaC = False
southamericaC = False
chosencontinents = [asia,antartica,northamerica,europe,oceania,africa, southamerica]
random.shuffle(chosencontinents)

for i in range (4):
    if chosencontinents [i] == asia:
        print "asia"
        asiaC = True
    elif chosencontinents [i] == antartica:
        print "antartica"
        antarticaC = True
    elif chosencontinents [i] == northamerica:
        print "northamerica"
        northamericaC = True
    elif chosencontinents [i] == europe:
        print "europe"
        europeC = True
    elif chosencontinents [i] == oceania:
        print "oceania"
        oceaniaC = True
    elif chosencontinents [i] == africa:
        print "africa"
        africaC = True
    elif chosencontinents [i] == southamerica:
        print "southamerica"
        southamericaC = True

while True:
    num = input ("Number: ")
    if (num == 1 and asiaC == True) or (num == 2 and antarticaC == True) or (num == 3 and northamericaC == True) or (num == 4 and europeC == True) or (num == 5 and oceaniaC == True) or (num == 6 and africaC == True) or (num == 7 and southamericaC == True):
        print "Yes"
    else:
        print "nop"
