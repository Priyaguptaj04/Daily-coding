num=int(input("Enter the number to be checked: "))
if num <= 1:
    print("Not prime")
else:
    for i in range(2,int(num**0.5) +1):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")