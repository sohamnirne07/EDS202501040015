def fibo(n): #function to calculate the nth Fibonacci number
    if n==0:  #base case: the 0th Fibonacci number is 0
        return 0 
    if n==1: #base case: the 1st Fibonacci number is 1
        return 1
    fibo1 = fibo(n-1) + fibo(n-2) #recursive call to calculate the nth Fibonacci number
    return fibo1

n = int(input("Enter a number: ")) #taking input
print(fibo(n)) #output the nth Fibonacci numbers