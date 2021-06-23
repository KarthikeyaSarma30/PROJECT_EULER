n=2**1000
sum=0
while n!=0 :
    r=n%10
    sum=sum+r
    n=n//10
print(sum)
