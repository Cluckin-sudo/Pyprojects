numbr = input("Input a number: ")
num = int(numbr)
if num > 1:
    for i in range(2,(num//2)+1):
        if num % i ==0:
            print("Not prime :(")
            break
        else:
            print("is prime")
            break
else: print ("enter a proper number!")