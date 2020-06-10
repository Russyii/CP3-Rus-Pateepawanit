Menulist = []
def showbill():
    total = 0
    print("======Russy Food======")
    for number in range(len(Menulist)):
        print(str(number+1)+".",Menulist[number][0],Menulist[number][1],"Baht")
        total += Menulist[number][1]
    print("Total is ",total,"Baht")

while True:
    MenuName = input("Please Enter Menu : ")
    if (MenuName.lower() == "exit"):
        break
    else:
        Price= int(input("Price : "))
        Menulist.append([MenuName,Price])

showbill()
