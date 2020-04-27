user = input("Enter Username : ")
password = input("Enter Password : ")
if user == "Lucy" and password == "Bangkok":
    print("Successful...")
    print("Hi",user+"!")
    print("-----Welcome-to-Russy-Cafe-----")
    print("What do you want for today?.....")
    print("**Cakes**")
    print("--------------------------------")
    print("1. Stawberry Cheesecake  >>60THB")
    print("2. Butter cake           >>45THB")
    print("**Coffee**")
    print("--------------------------------")
    print("3. Espresso              >>40THB")
    print("4. Cappuccino            >>50THB")
    print("5. Hot Late              >>45THB")
    print("6. Mocha                 >>40THB")
    userselect = int(input("Select menu : "))
    HowMuch = int(input("How much do you want? : "))
    if userselect == 1:
        print(60*HowMuch,"THB")
    elif userselect == 2:
        print(45*HowMuch,"THB")
    elif userselect == 3:
        print(40*HowMuch,"THB")
    elif userselect == 4:
        print(50*HowMuch,"THB")
    elif userselect == 5:
        print(45*HowMuch,"THB")
    elif userselect == 6:
        print(40*HowMuch,"THB")
    else:
        print("Error!!")
print("*****************THANK-YOU****************")

