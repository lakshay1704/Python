#sort a list of complex numbers from nearest distance to origin
#l = [1+2j,3+4j,5j,6+3j,10+20j,0.3+0.2j] this is working because i think sice all the elements of the list are complex
j = (-1)**0.5
l = [-4,6,3+4j,1+j,0] #this will not wirk until the above statement is defined
l = [10,9,8,7,6,5,4,3,2,1]
print(l)

#sort
n = len(l)
for i in range(len(l)):
    for j in range(0,n - i -1):
        if abs(l[i]) < abs(l[i+1]):
            l[i],l[i+1] = l[i+1],l[i]
        else:
            pass
print(l)
