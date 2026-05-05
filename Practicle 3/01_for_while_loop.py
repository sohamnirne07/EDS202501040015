n = int(input("Enter a number: ")) #taking input

# using for Loop
for i in range(1, n + 1): #loop from 1 to n
    print(i,end=" ")  #print the current number and stay on the same line
print() #print a new line after the for loop completes

# using while Loop
i = 1   #initialize 
while i <= n:  #loop until i is less than or equal to n
    print(i,end=" ") #print the current number and stay on the same line
    i += 1  #increment i by 1