import random

print("****WELCOME TO MANU UBER SERVICE***")
name = input("enter your name = ")
print("welcome to my uber app",name)
rider = ["a","b","c","d","e"]
list=[]
user=int(input("enter the number(1.book or 2.cancel"))
if user==1:
    print("your destination is confimed")
    limit = int(input("enter how much ride we have to do for you = "))
    index = 1
    total = 0
    while index <= limit:
        distance = int(input("enter how much far you will go distance in km = "))
        place = input("enter any place name = ")
        driver = random.choice(rider)
        print(driver,"this driver is available")
        if driver in rider:
            print("which driver you choice",driver,"he is on that distination",place)
            money = distance*5
            total += money
            print(index,"ride money = ",money)
        else:
            print("driver is not available")
            print(limit,"ride your total amount = ",total)

        index += 1
    list.append([driver,total])
    print(list)
    print("thank you to visit uber")
else:
    print("sorry!!your rider is cancelled")