def buzz_fizz(input):
    if input%3==0 and input%5==0:
        return "fizzbuzz"
    elif input%3==0:
        return "fizz"
    elif input%5==0:
        return "buzz"
    else:
        return input
print(buzz_fizz(10))

    
        