total=0
n=int(input("Enter the digits :")) 
original=n
while n>0:
    digit=int(n%10)
    total=total+digit
    n=n//10
print("the sum of digits of the given number ",original,"is",total)
