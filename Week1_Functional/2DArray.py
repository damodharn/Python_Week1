
row = int(input('Enter No of rows'))
col = int(input('Enter No of Columns'))
arr = [[0]*row]*col
for i in range(row):
    for j in range(col):
        arr[i][j] = int(input('Enter element for ', arr[i+1][j+1], 'position'))
print(arr)
