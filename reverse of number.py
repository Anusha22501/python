num=4321
print(str(num)[::-1])
or
num=1234
temp=num
reverse=0
while num>0:
    remainder=num%10
    reverse=(reverse*10)+remainder
    num=num//10
print(reverse)
