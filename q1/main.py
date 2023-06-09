def display():
    print("---------Welcome To Pauh Putra Supermarket-------")
    print("In Pauh Putra Supermarket You can Earn Points based on your Purchases")
    print("The higher The purchase amount the higher is your point.")


def receivesdata():
    display()
    purchaseamount = float(input("Please Enter Your Purchase Amount for This Month : RM "))
    points = 0
    if purchaseamount < 100:
        points += 0
    elif 100 <= purchaseamount < 200:
        points += 5
    elif 200 <= purchaseamount < 300:
        points += 15
    elif purchaseamount > 300:
        points += 30

    print(f"\n\nThe Points You Have accumulated is {points}")


if __name__ == '__main__':
    receivesdata()
