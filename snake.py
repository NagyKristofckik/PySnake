import time,os
sorszam = 1
elemszam = 1
map = [
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
    ["*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*", "*"],
]

def print_map(map):
    os.system("cls")
    for sor in map:
        for elem in sor:
            print(elem, end="  ")
        print()


sor_index = 7
oszlop_index = 7

lepes=[]

a=1
while a!=0:

    lepes.append(sor_index)
    lepes.append(oszlop_index)

    if len(lepes)>7:
        map[lepes[0]][lepes[1]] = "*"
        del lepes[0]
        del lepes[0]

    sor_index += -1
    oszlop_index += 0

    if sor_index>=15:
        sor_index=0
    if sor_index<=-1:
        sor_index=14
    if oszlop_index>=15:
        oszlop_index=0
    if oszlop_index<=-1:
        oszlop_index=14

    

    time.sleep(0.1)
           
    map[sor_index][oszlop_index] = "■"
    print("\n")
    print_map(map)
        