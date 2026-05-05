def nums(a): #defining a function to check if the number is even or odd
    if a%2==0: #checking if the number is divisible by 2 with no remainder
        print("the number is Even") #if the condition is true, print that the number is even
    else:
        print("The number is Odd") #if the condition is false, print that the number is odd

n = int(input("Enter a number: "))  #taking input from the user 
nums(n) #calling the function nums 