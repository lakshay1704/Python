#most number of eroes ina single row of a matrix
m = [[0,0,0],
         [4,0,0],
         [1,2,1]]
print(m)
#print(m[1])  #first row is at index 0
#print(len(m))
row = len(m)
for i in range(0,3,1):
    col = 0
    for j in m[i]:
        col+=1

print("number of rows -> ",row)
print("number of columns -> ",col)

max_num_zeros = 0
max_row_num = 0
for i in range(row):
    num_zeros = 0
    for j in range(col):
        if m[i][j] == 0:
            num_zeros+=1
        else:
            continue
    if max_num_zeros < num_zeros:
        max_num_zeros = num_zeros
        max_row_num = i+1
    else:
        continue

print("max row num ->",max_row_num)

