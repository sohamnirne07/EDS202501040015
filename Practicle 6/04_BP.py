import numpy as np #importing the numpy library
#creating two arrays to represent morning and evening blood pressure readings
morning = np.array([120, 130, 125, 110, 140])
evening = np.array([135, 128, 140, 125, 160])

bp = np.column_stack((morning, evening)) #combining the morning and evening readings into a single 2D array using the column_stack function
avg_bp = np.mean(bp, axis=0) #calculating the average blood pressure for morning and evening readings  
print("\nAverage BP (Morning, Evening):", avg_bp) #printing the average blood pressure for morning and evening readings
difference = evening - morning
print("\nDifference (Evening - Morning):", difference) #printing the difference between evening and morning blood pressure readings
increase = difference > 10
print("\nIncrease > 10:", increase) #printingwhich days had an increase in blood pressure greater than 10 between morning and evening readings
print("Days where increase >10:")
print(bp[increase])
combined = morning * evening #calculating the element-wise multiplication of morning and evening blood pressure readings
print("\nElement-wise Multiplication:", combined)#printing the result
max_bp = np.max(bp) #calculaItng max BP
print("\nMaximum BP Recorded:", max_bp) #printing max BP recorded

