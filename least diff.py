#return the indices of the numbers with least difference

l = [1,3,5,6,7,4,9]
x = 0
y = 0
min = 0
for i in range(0,len(l),1):
    for j in range(i):
        diff = l[i] - l[j]
        if diff < min:
            min = diff
            x = i
            y = j
        else:
            continue


print(x)
print(y)

