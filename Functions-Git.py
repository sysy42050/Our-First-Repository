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
