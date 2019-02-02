'''
-> You want to find all elements that exist in rows in the matrix.
#you want to find all the elements that exits in 50% or more rows in the given matrix

For example, given
'''
A =[
     [1, 2, 3, 5],
     [9, 2, 5, 9],
     [3, 2, 5, 8],
     [1 ,2 ,1 ,5],
     [5, 1, 3, 2]]
'''
the answer would be the row vector

 [1  2  3  5]
'''

n = []
for i in range(1,10,1):
    n.append(i)
ans = []
nc = {} #this dictionary consists of numbers as the key and the count of number of number in rows
#Below lines of code initializes the key values to 0
for i in n:
    nc[i] = 0
#print (nc)

#adding the count based on the number of rows
'''
for i in A:
    for j in i:
        c = 0
        if n[j] - c == 1:
            pass
        else:
            c+=1
'''
for i in A:
    for j in i:
        nc[j]+=1

print(nc)
#the below function counts the number of rows
n_r = 0
for i in A:
    n_r+=1
print('number of rows -> ',n_r)


final = []
for i in nc:
    if nc[i]>=n_r:
        final.append(i)

print(final)
