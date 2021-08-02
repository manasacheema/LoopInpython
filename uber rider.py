def riders(r):
    if r==1:
        print("rider1 is in modhinipuram")
    elif r==2:
        print("rider2 is in chivemla")
    elif r==3:
        print("rider3 is in suryapet")
    elif r==4:
        print("rider4 is in nalgonda")
riders(r=int(input("choose the rider \n 1.rider1 is in modhinipuram \n 2.rider2 is in chivemla \n 3.rider3 is in suryapet\n 4.rider4 is in knalgonda\n enter the rider")))
def booking(book):
    if book==1:
        print("yes,your booking is conform")
    elif book==2:
        print("cancle")
booking(book=int(input("select your rider \n 1.conform \n 2.cancle\n enter the option" )))
def distance(kms):
    i=0
    cash=0
    while i<kms:
        cash=kms*10
        i=i+1
    print("pay money",cash)
distance(kms=(int(input("enter your kms"))))
