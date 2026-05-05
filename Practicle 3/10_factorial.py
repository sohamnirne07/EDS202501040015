def fact(n): #defining a function to calculate the factorial of a number
    if n==1 or n==0: #base case: the factorial of 0 and 1 is 1
        return 1
    fact1 = n*fact(n-1) #recursive call to calculate the factorial 
    return fact1 

n = int(input("Enter a number: ")) #taking input from the user
print(fact(n)) #output the factorial of the number