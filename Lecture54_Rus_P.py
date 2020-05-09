def login():
    user = input("Enter Username : ")
    password = input("Enter Password : ")
    if user == "Tommy" and password == "ASDF":
        return "Hi "+user
    else:
        return login()
def showmenu():
    print("-----What do you want for today?-----")
    print("1. Thai Massage          >>>120/Hr")
    print("2. Incense Spa           >>>150/Hr")
    return ""
def selectmenu():
    userselect = int(input("Select menu : "))
    return Calculate(userselect)
def Calculate(user):
    if user == 1:
        One()
    elif user == 2:
        Two()
    else:
        selectmenu()
    return ''
def One():
    HowMuch = int(input("How many hours do you want? : "))
    How =120*HowMuch
    print("Total : ",120*HowMuch,"THB")
    return Vat(How)
def Two():
    HowMuch = int(input("How many hours do you want? : "))
    How = 150 * HowMuch
    print("Total : ",150*HowMuch,"THB")
    return Vat(How)
def Vat(price):
    Vat = 7/100
    result = price+(price*Vat)
    print("Vat include(7%) : ",result,"THB")

print("Welcome to Russy Massage & Spa")
print(login())
print(showmenu())
print(selectmenu())
print("-------------Enjoy!-------------")