


def prime(number):
    if number < 2:  # 0 and 1 are not prime numbers
        return False
    for i in range(2, int((number)) + 1):
        if number % i == 0:  # If divisible by any number other than 1 and itself
            return False
    return True  # It's prime

print(prime(6))  # Output: False
print(prime(7))



def prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
            break
    return True
print(prime(5))