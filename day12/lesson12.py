saxeli1 = input("Chaweret saxeli 1: ")
saxeli2 = input("Chaweret saxeli 2: ")
saxeli3 = input("Chaweret saxeli 3: ")
saxeli4 = input("Chaweret saxeli 4: ")

saxelebi = [saxeli1 , saxeli2, saxeli3, saxeli4]
damtvleli = 0
for element in saxelebi:
    if element[0] == "n":  #saxelebi[0] == "n"  --> nika == "n"
        damtvleli += 1
print("Mocemuli saxelebidan asobgera n-ze iwyeba {} saxeli".format(damtvleli))