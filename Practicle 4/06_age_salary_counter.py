from datetime import datetime #importing Datetime module
def age(birthday):           #defining a function to calculate age
    birthyear= int(birthday.split('-')[-1]) #splitting the input string by '-' and taking the last element as the birth year
    current_year = datetime.now().year #getting the current year using datetime module
    return current_year - birthyear  #calculating the age by subtracting the birth year from the current year and returning the result
    
def rupees_to_usd(rupees): #defining a function to convert rupees to dollars
    usd = 0.012*rupees  #converting rupees to dollars using the conversion rate
    return usd    #returning the converted amount in dollars

b = input("Enter Your birth date: ") #taking birth date as input 
c= int(input("Enter your salary in rupees: ")) #taking salary in rupees as input
print("Your age is :",age(b)) #calling the age function and passing input, then printing the result
print(f"Salary in Dollar is:{rupees_to_usd(c):.2f}") #calling the rupees_to_usd function and passing input, then printing the result formatted to 2 decimal places