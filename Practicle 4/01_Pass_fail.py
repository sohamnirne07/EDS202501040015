def grade(total_course,marks):    #defining a function grade
    if any (mark<40 for mark in marks):  #checking the passing criteria
        return 'Fail'
    agreegated_percentage= (sum(marks)/(100*total_course))*100 #calculating the agreegated_percentage
    print(f"Aggregated Percentage: {agreegated_percentage:.2f}") #print the agreegated_percentage upto 2 decimal
    #checking the grade criteria
    if agreegated_percentage>=75: 
        return 'Distinction'
    elif agreegated_percentage>=60:
        return 'First Class'
    elif agreegated_percentage>=50:
        return 'Second Class'
    elif agreegated_percentage>=40:
        return 'Third Class'

n = int(input("Enter the number of courses: ")) #taking input for number of courses
mark= list(map(int,input().split())) #taking input of mark from user and converting it in list of integers
print(grade(n,mark)) #printing the result of grade function
