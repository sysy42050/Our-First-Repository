# 4.13.3: Greeting
# Syann Hollins
# 2.6.19


name = input("What is your name: ")

def greetings():
    print("Hi there " + name + "!")
    print("Nice to meet you!")

greeting()


# 4.13.4: Functions and Variables
# Syann Hollins
# 2.14.19


x = 11

def print_something():
    x = 13
    print(x)

print_something()
print(x)


# 4.13.5: Functions and Variables-part 2
# Syann Hollins
# 2.14.19

my_variable = 3.6745

def something():
    print(my_variable + 10)

something()


# 4.13.6: Functions & variables, part 3
# Syann Hollins
# 2.18.19


def print_number(x):
    print(str(x))

print_number(12)
print_number('\n' + 'Hello World')


#4.14.4: Name & Age
# Syann Hollins
#2.18.19

def name_and_age(name, age):
    print('\n' 'Hi, my name is',name, 'and I am', str(age), 'years old.')

name_and_age('Syann', 15)
name_and_age('Sasha', 13)
name_and_age('George', 58)


# 4.14.5: Default Parameter Values
# Syann Hollins
# 2.19.19


def print_two_numbers(x, y = 20):
    print('First number:', x)
    print('Second number: ' + str(y))

print_two_numbers(5, 67)
print_two_numbers(23)

# 4.14.7: Print Multiple Times
# Syann Hollins
# 2.19.19

def print_multiple_times(string, times):
     for i in range(times):
         print(string)

print_multiple_times('Hello Computer Scientists', 4)

# 4.14.7: Print Multiple Times
# Syann Hollins
# 2.19.19

def print_multiple_times(string, times):
     for i in range(times):
         print(string)

print_multiple_times('Hello Computer Scientists', 4)


# 4.16.3: Enter a number
# Syann Hollins
# 2.20.19


try:
    my_number = int(input('Enter an  integer: '))
    print('Your number: ' + str(my_number))

except ValueError:
    print('That was not an integer')


# 4.16.4: Enter name and age
# Syann Hollins
# 2.20.19

name = input('What is your name: ')

age = -1

try:
    age = int(input('Enter your age: '))
except ValueError:
    print('That was not a valid age')

print('\n''Name: ', name)
print('Age:', age)


# 4.16.6: Temperature Converter
# Syann hollins
# 2.20.19

def celcius_to_fahrenheit(celcius):
    return celcius * 1.8 + 32

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit -32) / 1.8

try:
    c = float(input('Enter a temp in c: '))
    print('In F:', round(celcius_to_fahrenheit(c), 2))

    f = float(input('Enter a temp in f: '))
    print('In c: ', round(fahrenheit_to_celcius(f), 2))

except ValueError:
    print('You must enter a float!')

# 4.16.7: Enter a positive number
# Syann Hollins
# 2.21.19

def retrieve_positive_number():
    while True:
        try:
            number = int(input('Enter a positive number: '))
            if number > 0:
                return number
            else:
                print('That number was not positive')
        except ValueError:
            print('That was not a number.')

retrieve_positive_number()
