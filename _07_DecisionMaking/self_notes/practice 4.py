market=int(input("Enter the Market Price:"))
if market>10000:
    print("YOU GET DISCOUNT OF 20%")
if market>7000 and market<=10000:
    print("YOU GET DISCOUNT OF 15%")
if market<=7000:
    print("YOU GET DISCOUNT OF 10%")

