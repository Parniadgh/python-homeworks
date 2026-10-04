



weight=float(input("enter your weight in kilograms:"))
height=float(input("enter your height in meters:"))
bmi= weight/(height**2)

if bmi<18.5:
    print("you are underweight!!")
elif 18.5<=bmi<25:
    print("congratulations, you maintain a healthy weight")
elif 25<=bmi<30:
    print("you are overweight")
elif 30<= bmi:
    print("you are obese⚠")
else:
    print("eror,try again")
