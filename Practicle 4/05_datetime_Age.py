from datetime import datetime  #importing Datetime module 
n= int(input("Enter Your birth Year:  ")) #taking birth as input
current_year = datetime.now().year #getting the current year using datetime module
age = current_year - n #calculating the age by subtracting the birth year from the current year
print("Your age is: ",age) #printing the age of the user