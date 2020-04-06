# This Program wil identify whether a Number is Prime or Not

def PrimeNumber(num):
    for i in range(2,num,1):
        if num % i == 0:
            return False
            break
        else:
            continue
    return True

print('Enter an Integer Number :')
num = int(input())
if PrimeNumber(num) == True:
    print("Number {} : Prime".format(num))
else:
    print("Number {} : Non Prime".format(num))
