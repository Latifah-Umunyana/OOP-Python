
               
def year_of_birth(name,age):
    year = 2024 - age
    print(f"Hello {name}, you were born in {year}")


def my_country(country = "Uganda"):
    print(f"Hello AkiarChix from {country}")

def vowels_number(word):
    vowels = ['a','i','u','e','o']
    occurence = 0

    for i in word:
        if i in vowels:
            occurence += 1
    print(occurence)

def numbers(num_list):
    new_num_list = num_list.sort().reverse()
    print(new_num_list)

def greet(*names):
    for name in names:
        print(f"Hello {name}")
    

