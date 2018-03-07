#Hangman Game
#
#经典的猜字游戏。计算机随机选取一个单词，玩家要想办法把它一个字母一个字母
#地猜出来。如果玩家没能及时猜出那个单词，火柴小人就会被吊死了。

#模块引入
import random

#常量
HANGMAN=(
"""
第一次猜错
 
""",
"""
第二次猜错
""",
"""
第三次猜错
""",
"""
第四次猜错
""",
"""
第五次猜错
""",
"""
第六次猜错
""",
"""
第七次猜错
""",
"""
第八次猜错，Game Over!!!
"""
)




#玩家最多可以猜错多少次
MAX_WRONG=len(HANGMAN)-1

WORD=("OVERUSED","CLAM","GUAM","TAFFETA","PYTHON")

#初始化变量
word=random.choice(WORD)   #待猜的单词

so_far="-"*len(word)       #每条中横线表示word中的一个字母

wrong=0                   #玩家已经猜错的次数

used=[]                  #已经猜过的字母

#创建主循环
print("Welcome to Hangman.Good  luck!")

while wrong<MAX_WRONG and so_far!=word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far,the word is:\n",so_far)


#获取用户的答案
    guess=input("\n\nEnter your guess:")
    guess=guess.upper()
    
    while guess in used:
        print("You've already guessed the letter",guess)
        guess=input("Enter your guess:")
        guess=guess.upper()
    used.append(guess)

#判断猜测结果
    if guess in word:
        print("\nYes!",guess,"is in the word!")

        #创建新的so_far以包含guess
        new=""
        for i in range(len(word)):
            if guess ==word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far=new
    else:
        print("\nSorry,",guess,"isn't in the word.")
        wrong +=1

if wrong==MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hanged!")
else:
    print("\nYou guessed it!")
print("\nThe word was",word)
input("\n\nPress the enter key to exit.")
                

























