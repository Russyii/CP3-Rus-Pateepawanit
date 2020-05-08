def vatCal(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
print(vatCal(int(input("Enter Price : "))))