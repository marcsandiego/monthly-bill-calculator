#Seatwork: monthly bill calculator

package=input("Enter package [A,B,C]: ").upper()
while package not in ('A', 'B', 'C'):
    print("Invalid subscription package, please try again!")
    package=input("Enter package [A,B,C]: ").upper()
    
if package == 'A':
    month=int(input("Enter the month (in number): "))
    while not month in range(1, 13):
        print("Invalid number of month, please try again!")
        month=int(input("Enter the month (in number): "))
    if month in range(1, 13):
        if int == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            hours=int(input("Enter number of hours used: ")) 
            while hours > 744:
                print("Total no. of hours exceeded, please try again!")
                hours=int(input("Enter number of hours used: ")) 
            if hours<=744:
                if hours > 10:
                    additional=hours-10
                    total=float(200+(additional*15)) 
                    print("Total amount due in Php", total)
                else: 
                    print("Total amount due in Php 200.00")  
            else:
                print("Total no. of hours exceeded")

        elif month == 4 or 6 or 9 or 11:
            hours=int(input("Enter number of hours used: ")) 
            while hours > 720:
                print("Total no. of hours exceeded, please try again!")
                hours=int(input("Enter number of hours used: ")) 
            if hours<=720:
                if hours > 10:
                    additional=hours-10
                    total=float(200+(additional*15)) 
                    print("Total amount due in Php", total)
                else: 
                    print("Total amount due in Php 200.00")     
            else:
                print("Total no. of hours exceeded")    

        elif month == 2:
            hours=int(input("Enter number of hours used: ")) 
            while hours> 672:
                print("Total no. of hours exceeded, please try again!")
                hours=int(input("Enter number of hours used: "))
            if hours <= 672:    
                if hours > 10:
                    additional=hours-10
                    total=float(200+(additional*15)) 
                    print("Total amount due in Php", total)
                else: 
                    print("Total amount due in Php 200.00")               
            else:
                print("Total no. of hours exceeded")


if package == 'B':
    month=int(input("Enter the month (in number): "))
    while not month in range(1, 13):
        print("Invalid number of month, please try again!")
        month=int(input("Enter the month (in number): "))
    if month in range(1, 13):
        if int == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            hours=int(input("Enter number of hours used: ")) 
            while hours > 744:
                print("Total no. of hours exceeded, please try again!")
                hours=int(input("Enter number of hours used: ")) 
            if hours<=744:
                if hours > 20:
                    additional=hours-20
                    total=float(500+(additional*10)) 
                    print("Total amount due in Php", total)
                else: 
                    print("Total amount due in Php 500.00")
            else:
                print("Total no. of hours exceeded")

        elif month == 4 or 6 or 9 or 11:
            hours=int(input("Enter number of hours used: ")) 
            while hours > 720:
                print("Total no. of hours exceeded, please try again!")
                hours=int(input("Enter number of hours used: ")) 
            if hours<=720:
                if hours > 20:
                    additional=hours-20
                    total=float(500+(additional*10)) 
                    print("Total amount due in Php", total)
                else: 
                    print("Total amount due in Php 500.00")  
            else:
                print("Total no. of hours exceeded")    

        elif month == 2:
            hours=int(input("Enter number of hours used: ")) 
            while hours> 672:
                print("Total no. of hours exceeded, please try again!")
                hours=int(input("Enter number of hours used: "))
            if hours <= 672:    
                if hours > 20:
                    additional=hours-20
                    total=float(500+(additional*10)) 
                    print("Total amount due in Php", total)
                else: 
                    print("Total amount due in Php 500.00")              
            else:
                print("Total no. of hours exceeded")                

elif package == 'C':
        print("Total amount due is Php 900.00")
