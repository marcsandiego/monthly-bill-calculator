#Seatwork: monthly bill calculator

package=input("Enter package [A,B,C]: ").upper()
if package == 'A':
    month=int(input("Enter the month (in number): "))  
    if month in range(1, 13):
       hours=int(input("Enter number of hours used: ")) 
       if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
           if hours<=744:
               additional=hours-10
               total=float(200+(additional*15)) 
               print("Total amount due in Php", total)
           else:
               print("Total no. of hours exceeded")
       elif month == 4 or 6 or 9 or 11:
           if hours<=720:
               additional=hours-10
               total=float(200+(additional*15)) 
               print("Total amount due in Php", total)
           else:
               print("Total no. of hours exceeded")
       elif month == 2:
           if hours<=672:
               additional=hours-10
               total=float(200+(additional*15)) 
               print("Total amount due in Php", total)
           else:
               print("Total no. of hours exceeded")
       else:
           print("Enter a valid month.")
    else:
        print("Enter a valid month.")

elif package == 'B':
    month=int(input("Enter the month (in number): "))  
    if month in range(1, 13):
       hours=int(input("Enter number of hours used: ")) 
       if month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
           if hours<=744:
               additional=hours-20
               total=float(500+(additional*10)) 
               print("Total amount due in Php", total)
           else:
               print("Total no. of hours exceeded")
       elif month == 4 or 6 or 9 or 11:
           if hours<=720:
               additional=hours-20
               total=float(500+(additional*10)) 
               print("Total amount due in Php", total)
           else:
               print("Total no. of hours exceeded")
       elif month == 2:
           if hours<=672:
               additional=hours-20
               total=float(500+(additional*10)) 
               print("Total amount due in Php", (total,2))
           else:
               print("Total no. of hours exceeded")
       else:
           print("Enter a valid month.")
    else:
        print("Enter a valid month.")
    
    
elif package == 'C':
      print("Total amount due is Php 900.00")

else:
    print("Invalid subscription package, please try again!")
       

