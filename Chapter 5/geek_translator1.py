#Geek Translator
#演示字典的用法

choice=None
while choice !="0":
    print(
        """
        Geek Translator

        0 - Quit
        1 - Look Up a Geek Term
        2 - Add a Geek Term
        3 - Redefine a Geek Term
        4 - Delete a Geek Term
        """)

    choice=input("Choice:")
    print()
    #退出
    if choice=="0":
        print("Good-bye.")

    #得到定义
    elif choice=="1":
        term=input("What term do you want me to translate?:")
        if term in geek:
            definition=geek[term]
            print("\n",term,"means",definition)
        else:
            print("\nSorry,I don't know",term)
    #添加一对新的“术语/定义”
    elif choice=="2":
        term=input("What term do you want me to add?:")
        if term not in geek:
            definition=input("\n What's the definition?:")
            geek[term]=definition
            print("\n",term,"has been added.")
        else:
            print("\nThat term already exists! Try redefining it.")
    #重新定义一个已经存在的词汇
    elif choice=="3":
        term=input("What term do you want me to redefine?:")
        if term in geek:
            definition =input("What's the new definition?:")
            geek[term]=definition
            print("\n",term,"has been redefined.")
        else:
            print("\nThat term doesn't exist!Try adding it.")
    elif choice=="4":
        term=input("What term do you want me to delete?:")
        if term in geek:
            del geek[term]
            print("\nOkay,I deleted",term)
        else:
            print("\nI can't do that!',term,"doesn't exist in dictionary.")
    #未知选项
    else:
        print("\nSorry,but",choice,"isn't a valid choice.")
input("\n\n Press the enter key to exit.")




























        
