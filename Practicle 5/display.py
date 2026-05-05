number = [] #creating an empty list to store numbers
while True:   #starting an infinite loop to continuously prompt the user for input until they choose to quit
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Quit")
    n = int(input("Enter choice: ")) #taking input from the user and converting it to an integer to determine the user's choice
    if n==1:
        x = int(input()) #taking input from the user to add to the list
        number.append(x) #adding the user input to the end of the list
        print("List after adding: ",number) #printing the list after adding the new number
    elif n==2:   
        if len(number)==0:  #checking if the list is empty before trying to remove an element
            print("List is empty") #printing a message indicating that the list is empty
        else:
         x = int(input()) #taking input from the user to remove from the list
         if x in number:
             number.remove(x) #removing the user input from the list if it exists
         else:
             print("Element not found")#printing a message indicating that the element to be removed was not found in the list
    elif n==3:
        if len(number)==0: #checking if the list is empty before trying to display its contents
            print("List is empty") #printing a message indicating that the list is empty
        else:
            print(number) #printing the contents of the list if it is not empty
    elif n==4: 
        break #breaking the loop to quit the program
    else:
        print("Invalid Choice") #printing a message indicating that the user has entered an invalid choice