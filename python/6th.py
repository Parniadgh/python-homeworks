


total=int(input("enter the purchase amount:"))
shipping=input("standard shipping or express shipping?")


if shipping=="standard shipping":
    print(f"the total is {total+50000} toman")
    if total>20000000:
        print(f"{total}toman and free shipping")
elif shipping=="express shipping":
    print(f"the total is {total+100000}toman")
else:
    print("error")

