pno =  lambda x :"Positive" if x>0 else "Negative" if x<0 else "Zero" #defining a lambda function to check if a number is positive, negative or zero
n = float(input("enter the number : ")) # taking input from the user and converting it to a float
print(pno(n)) # calling the lambda function and passing the user input as an argument, then printing the result