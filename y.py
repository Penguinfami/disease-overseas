import random
#asia = 1
#antartica = 2
#northamerica = 3
#europe = 4
#oceania = 5
#africa = 6
#southamerica = 7

asiaC = 1
antarticaC = 2
northamericaC = 3
europeC = 4
oceaniaC = 5
africaC = 6
southamericaC = 7
chosencontinents = [asiaC,antarticaC,northamericaC,europeC,oceaniaC,africaC, southamericaC]
random.shuffle(chosencontinents)

for i in range (4):
    if chosencontinents [i] == asiaC:
        print "asia"
        asiaC = True
    elif chosencontinents [i] == antarticaC:
        print "antartica"
        antarticaC = True
    elif chosencontinents [i] == northamericaC:
        print "northamerica"
        northamericaC = True
    elif chosencontinents [i] == europeC:
        print "europe"
        europeC = True
    elif chosencontinents [i] == oceaniaC:
        print "oceania"
        oceaniaC = True
    elif chosencontinents [i] == africaC:
        print "africa"
        africaC = True
    elif chosencontinents [i] == southamericaC:
        print "southamerica"
        southamericaC = True

while True:
    num = input ("Number: ")
    if (asia and asiaC == True) or (antartica and antarticaC == True) or (northamerica and northamericaC == True) or (europe and europeC == True) or (australia and oceaniaC == True) or (africa and africaC == True) or (southamerica and southamericaC == True):
        print "Yes"
    else:
        print "nop"
