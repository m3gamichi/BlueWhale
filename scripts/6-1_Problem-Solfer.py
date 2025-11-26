#!/usr/bin/env python3
# GNU GENERAL PUBLIC LICENSE
# See the file 'LICENSE' for details
# ---------------------------------------------------------------------
# EN:
#     - Touch or modify the code below. If there is an error,
#     - please fix it and make a pull request ;)
from configs.util import *

states = {
    1: ["DOES IT WORK?", 0, 2, "DON' MESS WITH IT", ""],
    2: ["DID YOU MESS WITH IT?", 3, 6, "IDIOT", ""],
    3: ["DOES ANYONE ELSE KNOW?", 5, 4, "YOU STUPID FOOL", ""],
    4: ["CAN YOU HIDE IT", 0, 5, "", "YOU STUPID FOOL"],
    5: ["CAN YOU BLAME ANYONE ELSE?", 0, 5, "", "YOU STUPID FOOL"],
    6: ["WILL THEY BELIEVE YOU?", 0, 5, "DUMP IT SMARTLY", "YOU STUPID FOOL"],
}
state = 1
running = True
while running:
    if state == 0:
        print("NO PROBLEM!!")
        running = False
        Continue()
        break
    active_data = states[state]
    antwort = input(f"{active_data[0]} :")
    if antwort.startswith(("y","j")):
        state = active_data[1]
        print(active_data[3])
    else:
        state = active_data[2]
        print(active_data[4])