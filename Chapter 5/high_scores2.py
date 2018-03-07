#High Scores 2.0
#演示嵌套序列

scores=[]

choice=None
while choice !="0":
    print(
        """
        High Scores 2.0

        0 - Quit
        1 - List Scores
        2 - Add a Scores
        """
        )
    choice=input("Choice:")
    print()


    #退出
    if choice =="0":
        input("\n\nPress the enter key to exit.")
        print("Good-bye.")

    #显示高分表
    elif choice =="1":
        print("High Scores\n")
        print("NAME\tSCORE")
        for entry in scores:
            score,name=entry
            print(name,"\t",score)
    #添加一条得分记录
    elif choice== "2":
        name=input("What is the player's name?:")
        score=int(input("What score did the playere ger?:"))
        entry=(score,name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores=scores[:5]   #只保留最高的5条得分记录
    #无效选项
    else:
        print("Sorry,but",choice,"isn't a  valid choice.")



        
