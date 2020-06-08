Menulist = []
pricelist = []
def showbill():
    total = 0
    print("======Russy Food======")
    print("Invoid")
    print("**********************************************************************")
    for number in range(len(Menulist)):
        print(str(number+1)+'.',Menulist[number],pricelist[number],"Baht")
        total += pricelist[number]
    print("Total :",total,"Baht")
while True:
    MenuName = input("Please Enter Menu : ")
    if (MenuName.lower() == "exit"):
        break
    else:
        Price= int(input("Price : "))
        Menulist.append(MenuName)
        pricelist.append(Price)
showbill()
