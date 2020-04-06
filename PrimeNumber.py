# This Program wil identify whether a Number is Prime or Not

def PrimeNumber(num):
    for i in range(2,num,1):
        if num % i == 0:
            print('Number {} is NON PRIME'.format(num))
            break
        else:
            continue
    print('Number {} is PRIME'.format(num))

print('Enter an Integer Number :')
num = int(input())
PrimeNumber(num)
