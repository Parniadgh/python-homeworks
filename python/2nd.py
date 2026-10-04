


distance= float(input("enter the distance in kilometers:"))
taxi_fare= (distance*8000)+30000


if distance>=20:
    taxi_fare= (taxi_fare/100)*95
    print(f"{taxi_fare} toman")      ##in f"{} ro az daneshga yadam bood:))##
else:
    print(f"{taxi_fare} toman")

