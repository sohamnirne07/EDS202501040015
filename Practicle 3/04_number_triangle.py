n = int(input("Enter a number: "))  #taking input

for i in range(0, n):  #loop from 0 to n-1
    for j in range(0, i+1 ): #loop from 0 to i to print the numbers in each row
        print(j+1, end=" ") #print the current number (j+1) and stay on the same line
    print( ) #print a new line after each row of numbers is printed