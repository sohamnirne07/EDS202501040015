import numpy as np #importing the numpy library
#taking input from the user for the start, stop, and step values
start = int(input())
stop = int(input())
step = int(input())

sequence = np.arange(start,stop,step) #generating a sequence of numbers 

print(sequence)