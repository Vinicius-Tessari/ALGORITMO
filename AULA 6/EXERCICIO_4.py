def fizzbuzz(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return "FizzBuzz"
    elif numero % 3 == 0:
        return "Fizz"
    elif numero % 5 == 0:
        return "Buzz"
    else:
        return numero


print(fizzbuzz(15))
print(fizzbuzz(9))
print(fizzbuzz(10))
print(fizzbuzz(7))