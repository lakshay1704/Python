#create time tables
'''
l = [ 1 2 3 4 5
        2 4 6 8 10
        3 6 9 12 15
        4 8 12 16 20 ]
 here n = 5
'''
l = []
n = int(input('Enter the value of n'))
for i in range(1,n+1,1):
    el = []
    for j in range(1,n+1,1):
        el.append(i*j)
    l.append(el)
    

print(l)
