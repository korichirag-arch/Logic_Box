print("\033[1;36m___________________________________________________________________________________________________________________________________________\033[0m")
print("\n\033[1;33mWelcome to the Logic box Program 🙏. \nThis program will help you Pattern generate and Number analyzer.\033[0m")
print("\033[1;36m___________________________________________________________________________________________________________________________________________\033[0m")
while True:
 print("\033[1;36m___________________________________________________________________________________________________________________________________________\033[0m")
 print("\n\033[1;32mPress 1 for Pattern Generator\033[0m")
 print("\033[1;32mPress 2 for Number Analyzer\033[0m")
 print("\033[1;32mPress 3 for Exit\033[0m")
 print("\033[1;36m___________________________________________________________________________________________________________________________________________\033[0m")

 choice =int(input("\nENTER YOUR CHOICE: "))
 print("\033[1;36m___________________________________________________________________________________________________________________________________________\033[0m\n")

 match choice:
    case 1:
            print("\033[1;32mPress 1 for Right angle triangle pattern.\033[0m")
            print("\033[1;32mPress 2 for Left angle triangle pattern.\033[0m")
            print("\033[1;32mPress 3 for Inverted Pyramid pattern.\033[0m")
            print("\033[1;32mPress 4 for Pyramid pattern.\033[0m")
            c=int(input("\nENTER YOUR CHOICE: "))
            if c==1:
                n=int(input("\nEnter the number of rows: "))
                for i in range(1,n+1):
                    for j in range(i):
                        print("\033[1;45m*\033[0m",end="   ")
                    print()
            elif c==2:
                n=int(input("\nEnter the number of rows: "))
                for i in range(n,0,-1):
                    for j in range(n-i):
                        print(" ", end="  ")
                    for j in range(i):
                        print("\033[1;41m*\033[0m", end="  ")
                    print()
            elif c==3:
                n=int(input("\nEnter the number of rows: "))
                for i in range(n,0,-1):
                    for j in range(n-i):
                        print(" ", end=" ")
                    for j in range(2*i-1):
                        print("\033[1;43m*\033[0m", end=" ")
                    print()
            elif c==4:
                n=int(input("\nEnter the number of rows: "))
                for i in range(1,n+1):
                    for j in range(n-i):
                        print(" ", end=" ")
                    for j in range(2*i-1):
                        print("\033[1;40m*\033[0m", end=" ")
                    print()
            else:
                print("\033[1;31mInvalid choice. Please try again.\033[0m\n")
    case 2:
        s=int(input("Enter the start of the range: "))
        e=int(input("Enter the end of the range: "))
        if s<e:
            print(f"\033[1;33mNumber {s} is odd.\033[0m") if s%2 else print(f"\033[1;34mNumber {s} is even.\033[0m")
            for i in range(s+1,e+1):
                if i%2:
                    print(f"\033[1;33mNumber {i} is odd.\033[0m")
                else:
                    print(f"\033[1;34mNumber {i} is even.\033[0m")
            sum=0
            while s<=e:
                sum+=s
                s+=1
            print(f"\033[1;32mThe sum of numbers is: {sum}\n\033[1;0m")
        else:
            print("\033[1;31mInvalid range. Please ensure that the start of the range is less than the end.\033[0m\n")
    case 3:
        print("\033[1;36m___________________________________________________________________________________________________________________________________________\033[0m")
        print("\n\033[1;33mThank you for using the Logic box Program 🙏. \nWe hope you enjoyed the experience and learned something new about yourself 😊.\033[0m")
        print("\033[1;36m___________________________________________________________________________________________________________________________________________\033[0m\n")
        break
    case _: 
        print("\033[1;31mInvalid choice. Please try again.\033[0m\n")
   
            