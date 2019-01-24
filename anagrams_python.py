#testing panagrams

#s = 'the quik brown fox jumps over the lazy dog'
s = 'pack my box with five dozen liquor jugs'
l = []
s_edit = ''
'''
for i in range(65,91,1):
    l.append(i)
'''
for i in range(97,123,1):
    l.append(i)
#print(l)
#print(len(l))
for i in s:
    if i == chr(32):
        pass
    else:
        s_edit+=i
#print(s_edit)
#print(len(s_edit))
def check(s_edit,l):
    for i in l:
        c = 0
        for j in s_edit:
            if chr(i) == j:
                #print(chr(i) + ' found')
                break
            else:
                #print(chr(i)+' not found')
                c+=1
                continue
        if c>=len(s_edit):
            return False
            break
        else:
            continue
    return True
#print(c)
ans = check(s_edit,l)
print(ans)
    
