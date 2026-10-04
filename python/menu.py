


bill=[]
restaurant_bill=[]
beverages_bill=[]


print("welcome to the best restaurant in town,look at our special offer on persian foods")

while True:
    restaurant=input("1.food 2.beverages 3.exit:")
    
    match restaurant:
        case"1":
            
            food=input("1.persian food 2.italian food 3.exit:")
            
            match food:
               case"1":
                   while True:
                    persian_food=input("1.shishlik 2100 2.kabab 1500 3.jooje 1300 4.maahi 1800 5.gheime 1200 6.exit:")
                    match persian_food:
                      case "1":
                         num_shishlik=int(input("how many portions would you like?:"))
                         price_shishlik=num_shishlik*2100*1.1

                         if num_shishlik>3:
                            price_2_shishlik=price_shishlik*0.75
                            restaurant_bill.append(price_2_shishlik)
                          
                         else:
                            restaurant_bill.append(price_shishlik)
                        

                         
                      case"2":
                               num_kabab=int(input("how many portions would you like?:"))
                               price_kabab=num_kabab*1500*1.1
                               if num_kabab>4:
                                 price_2_kabab= price_kabab*0.75
                                 restaurant_bill.append(price_2_kabab)
                               else:
                                restaurant_bill.append(price_kabab)
                        
                        
                      
                      case"3":
                               num_jooje=int(input("how many portions would you like?"))
                               price_jooje=num_jooje*1300*1.1
                               if num_jooje>5:
                                 price_2_jooje= price_jooje*0.75
                                 restaurant_bill.append(price_2_jooje)
                               else:
                                restaurant_bill.append(price_jooje)

                       
                      case"4":
                               num_maahi=int(input("how many portions would you like?:"))
                               price_maahi=num_maahi*1800*1.1
                               if num_maahi>4:
                                  price_2_maahi= price_maahi*0.75
                                  restaurant_bill.append(price_2_maahi)
                               else:
                                restaurant_bill.append(price_maahi)

                         
                      case"5":
                               num_gheime=int(input("how many portions would you like?:"))
                               price_gheime=num_gheime*1200*1.1
                               if num_gheime>6:
                                 price_2_gheime= price_gheime*0.75
                                 restaurant_bill.append(price_2_gheime)
                               else:
                                restaurant_bill.append(price_gheime)
                         
                      case"6":
                               break
            
        
               case"2":
                     while True:
                      italian_food=input("1.pasta 1300 2.pizza 1800 3.lasagna 1500 4.risotto 1600 5.spaghetti 1300 6.exit:")
                      match italian_food:
                        case"1":
                           num_pasta=int(input("how many portions would you like?:"))
                           price_pasta=num_pasta*1300*1.1
                           restaurant_bill.append(price_pasta)
                    
                        case"2":
                           num_pizza=int(input("how many portions would you like?:"))
                           price_pizza=num_pizza*1800*1.1
                           restaurant_bill.append(price_pizza)  
                    
                        case"3":
                           num_lasagna=int(input("how many portions would you like?:"))      
                           price_lasagna=num_lasagna*1500*1.1
                           restaurant_bill.append(price_lasagna)   
                  
                        case"4":
                           num_risotto=int(input("how many portions would you like?:")) 
                           price_risotto=num_risotto*1600*1.1
                           restaurant_bill.append(price_risotto)   
                     
                        case"5":
                           num_spaghetti=int(input("how many portions would you like?:"))     
                           price_spaghetti=num_spaghetti*1300*1.1
                           restaurant_bill.append(price_spaghetti)
                   
                        case"6":
                           break
            
              
            
    match restaurant:
        case"2":
             
           beverages=input("1.persian beverages 2.non-persian beverages 3.exit")   

           match beverages:
                 case"1":
                    while True:
                     persian_beverages=input("1.doogh 120 2.tea 100 3.sharbat 200 4.sahlab 200 5.khakeshir 180 6.exit") 
                     match persian_beverages:
                       case"1":
                          num_doogh=int(input("how many would you like?:"))  
                          price_doogh=num_doogh*120*1.1
                          beverages_bill.append(price_doogh)
                    
                       case"2":
                          num_tea=int(input("how many would you like?"))
                          price_tea=num_tea*100*1.1
                          beverages_bill.append(price_tea)
                 
                       case"3":
                          num_sharbat=int(input("how many would you like?:"))
                          price_sharbat=num_sharbat*200*1.1
                          beverages_bill.append(price_sharbat)
                   
                       case"4":
                          num_sahlab=int(input("how many would you like?:"))
                          price_sahlab=num_sahlab*200*1.1
                          beverages_bill.append(price_sahlab)
                  
                       case"5":
                          num_khakeshir=int(input("how many would you like?"))
                          price_khakeshir=num_khakeshir*180*1.1
                          beverages_bill.append(price_khakeshir)
              
                       case"6":
                          break
           
           
                 case"2":
                    while True:
                     nonpersian_beverages=input("1.espresso 200 2. affogato 300 3.hot chocolate 250 4.cappuccino 350 5.pistachio latte 450 6.exit")
                     match nonpersian_beverages:
                       case"1":
                          num_espresso=int(input("how many would ypu like?:"))
                          price_espresso=num_espresso*200*1.1
                          beverages_bill.append(price_espresso)
                    
                       case"2":
                          num_affogato=int(input("how many would ypu like?:"))
                          price_affogato=num_affogato*300*1.1
                          beverages_bill.append(price_affogato)
                 
                       case"3":
                          num_hotchocolate=int(input("how many would you like?:"))
                          price_hotchocolate=num_hotchocolate*250*1.1
                          beverages_bill.append(price_hotchocolate)
                  
                       case"4":
                          num_cappuccino=int(input("how many would you like?:"))
                          price_cappuccino=num_cappuccino*350*1.1
                          beverages_bill.append(price_cappuccino)
                    
                       case"5":
                          num_pitachiolatte=int(input("how many would you like?:"))
                          price_pistachiolatte=num_pitachiolatte*450*1.1
                          beverages_bill.append(price_pistachiolatte)
                    
                       case"6":
                          break
   
    match restaurant:
        case"3":
           bill.append(sum(restaurant_bill) + sum(beverages_bill))  ##in ghesmat ro search kardam ke befahmam chejoori jam konam#
           print(bill)
           break

                            
                                 
                 
 
                                                


