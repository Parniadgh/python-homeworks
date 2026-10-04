
final_list=[]
log_in_list=["parniadehghani","parnia1234"]

while True:
    menu=input("1.sign in 2.sign up 3.exit")
    match menu:
        case"1":
            list_1=[]
            username_1=input("enter your username:")
            password_1=input("enter your password:")
            if username_1 and password_1 in log_in_list:
                print("logged in succesfully")
            else:
                print("wrong information,try again")
                break
            
            python_1=float(input("enter your python score:"))
            java_1=float(input("enter your java score:"))
            html_1=float(input("enter your html score:"))
            list_1.append(("uername:",username_1))
            list_1.append(("password:",password_1))
            list_1.append(("python score:",python_1))
            list_1.append(("java score:",java_1))
            list_1.append(("html score:",html_1))
            final_list.append(list_1)
            print(final_list)
    match menu:
        case "2":
            list_2=[]
            username_2=input("enter your username:")
            password_2=input("enter your password:")
            print("welcome to MFT🤓")
            python_2=float(input("enter your python score:"))
            java_2=float(input("enter your java score:"))
            html_2=float(input("enter your html score:"))
            list_2.append(("uername:",username_2))
            list_2.append(("password:",password_2))
            list_2.append(("python score:",python_2))
            list_2.append(("java score:",java_2))
            list_2.append(("html score:",html_2))
            final_list.append(list_2)
            print(final_list)
    match menu:
        case"3":
            print("Bye bye")
            break


            



