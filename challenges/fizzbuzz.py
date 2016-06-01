def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"

    if num % 3 == 0:
        return "Fizz"

    if num % 5 == 0:
        return "Buzz"

    return str(num)


numbers = list(range(1, 101))
print(numbers)

fizzbuzz_numbers = [fizzbuzz(num) for num in numbers]
print(fizzbuzz_numbers)
