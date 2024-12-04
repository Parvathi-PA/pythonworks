

def is_armstrong(number):
    total=0
    length=len(str(number))
    # length=int(length)
    while number!=0:
      digit=number%10
      product=digit**length
      total=total+product
      number=number//10
    return  total

print(is_armstrong(153))