inp=open('input.txt', 'r')
out=open('output.txt', 'w')
#s=inp.read()
s=input()
temp=''
t=1
ans=0
for i in s+' ':
    if i in '0123456789':
        temp+=i
    else:
        if temp!='':
            ans+=int(temp)*t
            temp=''
            t=1
        if i=='-': t=-1
print(ans)
inp.close()
out.close()