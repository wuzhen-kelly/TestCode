#Global Reach
#演示全局变量

def read_global():
    print("From inside the local scope of read_global(),value is:",value)

def shadow_global():
    value=-10
    print("From inside the local scope of shadow_global(),value is:",value)

def change_global():
    global value
    value=-10
    print("From inside the local scope of change_global(),value is:",value)

#程序主体
#value是个全局变量，因为我们现在是在全局作用域里面
value=10
print("In the global scope,value has been set to:",value,"\n")

read_global()
print("Back in the global scope,value is still:",value,"\n")

shadow_global()
print("Back in the global scope,value is still:",value,"\n")

change_global()
print("Back in the global scope,value has now changed to:",value)


input("\n\nPress the enter key to exit.")
