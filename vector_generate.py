#Generate a vector like 1,2,2,3,3,3,4,4,4,4

n = int(input('Enter the value of n'))
l = []
while n!=0:
    for i in range(1,n+1,1):
        l.append(n)
    n-=1
ne = []
for j in range(-1,-(len(l)+1),-1):
    ne.append(l[j])
#print(l)
print(ne)
