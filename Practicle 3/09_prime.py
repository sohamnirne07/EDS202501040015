def prime(num): #defining a function to check if the number is prime or not 
    if num >1: #checking if the number is greater than 1
        for i in range(2,num): #loop from 2 to num-1 to check if num is divisible
            if(num%i==0): #checking if num is divisible by i with no remainder
                print(f"{num} is not a prime number") #if the condition is true, print that num is not a prime number and exit the loop
                break  #if num is divisible by any number in the range, we break the loop
        else:
         print("The number is prime.") #if num is not divisible by any number in the range, so we print that num is a prime number
n = int(input("Enter a number: ")) #taking input from the user
prime(n) #calling the function prime