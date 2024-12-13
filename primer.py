#prime number
n=int(input("enter number:"))
c=0
for i in range(1,n+1):
    if n%i==0:
        c+=1
if c==2:
    print("prime")
else:
    print("Not prime")
#even number
n=int(input("enter number:"))
for i in range(1,n+1):
    if(i%2==0):
        print(i)