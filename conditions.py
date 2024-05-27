

def print_numbers(n):
    numbers = range(n)
    for number in numbers:
        print(number)

print_numbers(10)
# print_numbers(100)
# print_numbers(1000)

def print_odd_numbers(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 != 0:
            print(number)

print_odd_numbers(10)

def odd_or_even(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 ==0:
            print(f"{number} is even")
        else:
            print(f"{number} is not even")

odd_or_even(10)

def check_divisibility(n):
    numbers = range(n)
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is divisible by 2")
        elif number % 3 == 0: 
            print(f"{number} is divisible by 3")
        elif number% 5 == 0:
            print(f"{number} is divisible by 5")
        else:
            print(f"{number} is not divible by 2,3 or 5")
check_divisibility(10)

def fizz_buzz(n):
    numbers = range(n)
    for number in numbers:
        if number %3 == 0 and number %5 == 0:
            print("fizzbuzz")
        elif number % 3 == 0:
            print("fizz")
        elif number % 5 == 0:
            print("buzz")
        else:
            print(f"{number} is not divisible by 3 or 5")
fizz_buzz(16)

def countdown (n):
    while n>0:
        print(n)
        n -= 1

countdown(10)

def count_down_to_five(n):
    while n > 0:
        print(n)
        if n == 5:
            break
        n -= 1
count_down_to_five(10)

def divisible_by_seven(n):
    x= 0
    while x <= n:
        x += 1
        if x % 7 != 0:
            continue
        print(f"{x} is divible by 7")
divisible_by_seven(10)


# def odds(): 
#     x = 0
#     while x < 10: 
        
#         if x % 2 != 0: 
#              continue 
#         print(f"{x} is an even number") 
#         x += 1
       

# odds()


