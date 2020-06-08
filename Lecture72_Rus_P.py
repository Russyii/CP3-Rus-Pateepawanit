Menulist = []
def showbill():
    print("======Russy Food======")
    for number in range(len(Menulist)):
        print(Menulist[number][0],Menulist[number][1])

while True:
    MenuName = input("Please Enter Menu : ")
    if (MenuName.lower() == "exit"):
        break
    else:
        Price= int(input("Price : "))
        Menulist.append([MenuName,Price])

showbill()
