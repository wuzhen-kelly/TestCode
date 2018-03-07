# Mood Computer
# 演示elif语句

import random

print("I sense your energy. Your true enotions are coming across my screen.")

print("You are...")

mood = random.randint(1,3)

if mood ==1:
    #高兴
    print("Happy")
elif mood ==2:
    #一般
    print("general")
elif mood ==3:
    #难过
    print("sad")
else:
    print("Illegal mood value!(You must be in a really bad mood).")

print("..today.")

input("\n \n Press the enter key to exit.")
    
