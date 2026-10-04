



age= float(input("enter your age:"))
day= str(input("enter a day of the week:"))
base_ticket_price= 200000


if 1<=age<12:
    print((base_ticket_price/100)*50, "toman")
elif 60<=age:
    print((base_ticket_price/100)*70, "toman")
elif day=="tuesday":
    print((base_ticket_price/100)*80 ,"toman")
else:
    print(f"{base_ticket_price} toman")

