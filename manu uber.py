import random
print("*************WELCOME TO MANU UBER SERVICE*************")
name = input("enter your name = ")
print("welcome to manu uber app",name)
rider=["a","b","c","d","e"]
list=[]
user=int(input("enter a number(1.book or 2.cancel"))
if [ user==1]:
    print("your destination is confimed")
    limit=int(input("enter how much rider has to enter to you= "))
    index = 1
    total = 0
    while index <=limit:
        distance =int(input("enter how much far you will go distance in km = "))
        place = input("entr any place name =")
        driver = random.choice(rider)
        print(driver,"this driver is avaiaable")
        if driver in rider:
           print("which driver you choose",driver,"he is on that destination", place)
           money=destination*5
           total+=money
           print(index,"ride money=",money)
        else:
               print("driver is not avaialable")
               print(limit,"ride your total amount=",total)
        index +=1
        list.append([driver,total])
        print(list)
        print("thank you to visit manu uber")
    else:
        print("sorry!!your ride is cancelled")
    









 