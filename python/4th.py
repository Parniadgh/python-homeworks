


temperature = int(input("enter the temperature:"))
rain= input("Is it rainy outside?")

if temperature<0:
    print("put on a thick jacket")
elif 0<=temperature<=10:
    print("wear warm clothes")
elif 11<=temperature<25:
    print("it is mild outside")
else:
    print("wear cool clothes")

if rain=="yes":
    print("do not forget to take your umbrella")