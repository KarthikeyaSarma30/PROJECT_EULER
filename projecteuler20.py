factorial=1
for i in range(1,101) :
  factorial=factorial*i
sum=0
while factorial!=0 :
  r=factorial%10
  sum=sum+r
  factorial=factorial//10
print(sum)
