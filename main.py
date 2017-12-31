import random as rdm
import re
import easygui as ee

file = open("data/questions.txt",'r')
list = []
for e in file:
    list.append(e)
file.close()

file = open("data/players.txt",'r')
players = []
for e in file:
    players.append(e)
file.close()
for i in range(len(players)):
    players[i] = players[i].replace('\n',"")
p = re.compile("PLAYER",)
title = "Ultimate Picolo of doom"
bool = True
while bool == True :
    txt = list[rdm.randint(0, len(list) - 1)]
    for i in range(txt.count("PLAYER")):
        txt = p.sub(players[i], txt, count=1)
    rdm.shuffle(players)
    if ee.ccbox(txt, title):
        pass
    else:
        bool = False