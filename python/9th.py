



food=str(input("select your food:"))
number=int(input("how many?"))



if food=="pizza":
    price=250000*number
    print(f"{price}toman")
if food=="burger":
    price=180000*number
    print(f"{price}toman")
if food=="sandwich":
    price=120000*number
    print(f"{price} toman")
if price>500000:
    print("a drink is on us")
else:
    print("it's out of the menu")

