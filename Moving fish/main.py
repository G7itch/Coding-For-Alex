import os
import time

file = open("fish.txt","r")
content = file.readlines()
file.close()

indents = 2
fish1 = content[0:4]
fish2 = content[5:9]
print(fish1)
print(fish2)
currentfish = fish1

while True:
    os.system("clear")
    if indents == 0:
        currentfish = fish1
        indents += 1
    elif indents == 5:
        currentfish = fish2
        indents -= 1
    for line in currentfish:
        print("/t"*indents,line)
    time.sleep(2)