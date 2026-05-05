def pn(a): #defining a function to check if the number is positive, negative or zero
    if a>0: #checking if the number is greater than 0
        print("the number is Positive") #if the condition is true, print that the number is positive
    elif(a<0): #checking if the number is less than 0
        print("The number is Negative") #if the condition is true, print that the number is negative
    else:
        print("The number is Zero") #if the number is neither positive nor negative, it must be zero, so print that the number is zero

n = int(input("Enter a number: ")) #taking input from the user
pn(n) #calling the function pn 