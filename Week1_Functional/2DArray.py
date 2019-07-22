# *********************************************************************************************
# Purpose: To create a library for reading in 2D arrays of integers, doubles, or booleans from
#           standard input and printing them out to standard output.
# Author:  Damodhar D. Nirgude.
#  ************************************************************************************************
row = int(input('Enter No of rows'))
col = int(input('Enter No of Columns'))
arr = [[0]*row]*col  # Creating an array of User defined no of rows and columns.
for i in range(row):
    for j in range(col):
        arr[i][j] = int(input('Enter element for ', arr[i+1][j+1], 'position'))  # Accepting elements from user into the array.
print(arr)
