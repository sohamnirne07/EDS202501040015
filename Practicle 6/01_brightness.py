import numpy as np #importing the numpy library 
arr = np.random.randint(0,255,size=(5,5)) #creating a 5x5 array of random integers between 0 and 255 using the randint function from the numpy library
print(arr)  #printing the original array
result = np.clip(arr+30,0,255) #adding 30 to each element of the array and then using the clip function to limit the values between 0 and 255
avg = np.mean(result) #calculating the average of the resulting array using the mean function from the numpy library
print(avg)