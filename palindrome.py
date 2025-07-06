num=int(input("enter the number to be checked:"))
original=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

if rev == original:
        print ("the given number is a palindrome")
else:
        print("the given number is not a palindrome")
