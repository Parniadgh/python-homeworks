


age= float(input("enter your age:"))
if age<18:
    print("Bye Bye, you are not allowed!")
else :
    username=input("enter your username:")
    password= input("enter your password:")
    if username=="dark shadow" and password=="King Arthur 7300":
        print("logged in successfully")
    elif username!="dark shadow" and password=="King Arthur 7300":
        print("wrong username, try again!")
    elif username=="dark shadow" and password!="King Arthur 7300":
        print("wrong password,try again!")
    else:
        print("Sorry,both username and password are wrong")