days=int(input("Enter the number of days:"))
if days<=5:
    charges=days*2
    print("total charge is:",charges)
elif days>6 and days>=10:
    charges=days*3
    print("Total charge is:",charges)
elif days>11 and days>=15:
    charges=days*4
    print( "Total charge is:",charges)
elif days>15:
    charges=days*5
    print( "Total charge is:",charges)
else:
    if days==0:
        print("no charges")

