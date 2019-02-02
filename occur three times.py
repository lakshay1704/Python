'''

Problem 39. Which values occur exactly three times?
Created by Cody Team in Cody Challenge


Return a list of all values (sorted smallest to largest) that appear exactly three times in the input vector x. So if
'''
x = [1, 2, 5, 2, 2, 7, 8, 3, 3, 1, 3, 8, 8, 8,5,5]
'''
then

 y = [2 3]


'''
n = {}
a = -20
while a!=21:
    n[a] = 0
    a+=1
#print(n)
for i in x:
    for j in n:
        if i == j:
            n[i]+=1
        else:
            pass

print(n)
final = []
for i in n:
    if n[i] == 3:
        final.append(i)

print(final)

