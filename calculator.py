
def add(a,b):
    answer = a + b
    return answer

def subtract(a,b):
    answer = a - b
    return answer

def multiply(a,b):
    answer = a * b
    return answer

def divide(a,b):
    answer = a/b
    return answer

def remainder(a,b):
    answer = a % b
    return answer

def power_of(a,b):
    answer = a ** b
    return answer

def whole_division(a,b):
    answer = a // b
    return answer

def sum(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total    

def multiplication(*numbers):
    product = 1
    for number in numbers:
        product *= number
    return product
    

def create_sentence(**words):
     print(words)
     sentence = ""
     for word in words.values():
        sentence += word
        sentence += " "
     return sentence    

def sum_and_greet(*args,**kwargs):
    total = 0
    for number in args:
        total += number
    greeting = f"Hello {kwargs['first_name']} {kwargs['last_name']}, The sum of {list(args)} is {total}"
    return greeting


print(add(2,3))
print(subtract(2,3))
print(divide(2,3))
print(multiply(2,3))
print(create_sentence(a="I",b="Love",c="AkiraChix",d="in",e="Nairobi"))
print(sum_and_greet(10,20,30,first_name = "Latifa",last_name = "Umunyana"))
print(sum_and_greet(40,50,70,200,1000,first_name = "Shania",last_name = "Niwemwiza"))
