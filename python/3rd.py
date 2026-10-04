


electricity_consumption=float(input("enter the electricity consumption:"))

if 0<=electricity_consumption<=100:
    payment= electricity_consumption*1000
    print(f"{payment} toman")

elif 101<=electricity_consumption<=200:
    payment= electricity_consumption*1500
    print(f"{payment} toman")

elif electricity_consumption>200:
    payment= electricity_consumption*2500
    print(f"{payment} toman")

    
     
 
