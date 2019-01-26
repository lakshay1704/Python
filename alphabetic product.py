'''

Problem 42. Find the alphabetic word product
Created by Cody Team in Cody Challenge


If the input string s is a word like 'hello', then the output word product p is a number based on the correspondence a=1, b=2, ... z=26. Assume the input will be a single word, although it may mixed case. Note that A=a=1 and B=b=2.

So
'''
s = 'lakshay'
'''
means

 p = 8 * 5 * 12 * 12 * 15 = 86400

Bonus question: How close can you get to a word product of one million?

'''

s_edit = ''
for i in s:
    if ord(i)>=65 and ord(i)<=95:
        x = ord(i)+32
        s_edit+=chr(x)
        #print(s_edit)
    else:
        #print(s_edit)
        s_edit+=i
#print(s_edit)

t1 = []
t2 = []
d = {}
for i in range(97,123,1):
    #t1.append(i)
    t2.append(chr(i))
    #d[i] = chr(i)

#print(t1)
#print(t2)
#print(d)
for i in range(1,27,1):
    t1.append(i)

#print(t1)
#print(t2)
for i in range(1,27,1):
    d[t2[i-1]] = i

#print(d)
product = 1
for i in s_edit:
    product*=d[i]

print(product)
