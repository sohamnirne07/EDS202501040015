import numpy as np #importing the numpy library 
row,colm = map(int,input().split()) #taking input from the user for the number of rows and columns in the matrix, and converting them to integers using the map function
if row==0 and colm==0:  #checking if the user input for rows and columns is zero
	matrix = np.empty((row,colm), dtype = int) #creating an empty matrix of the specified size using the empty function
else:
	matrix = np.array([input().split()for i in range(row)],dtype=int) #creating a matrix by taking input from the user for each row, splitting the input into individual elements
print(matrix) #printing the matrix
print(np.ndim(matrix)) #calculating the number of dimensions of the matrix using the ndim 
print(np.shape(matrix)) #calculating the shape of the matrix using the shape function
print(np.size(matrix)) #calculating the total number of elements in the matrix using the size function