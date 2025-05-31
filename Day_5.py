#for loops

fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
print("hello")

#Highest Score
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

total=sum(student_scores)
print(total)
total =0
for sum in student_scores:
    total+=sum
    print(total)

print(max(student_scores))

largest = 0
for num in student_scores:
    if num > largest:
        largest=num

print(f"The largest number is:{largest}")

#for loop with range

# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)

for number in range(1,101):
    if (number % 3 == 0) and (number % 5 == 0):
        print('FizzBuzz')

    elif number % 5 == 0:
        print('Buzz')

    elif number % 3 == 0:
        print('Fizz')

    else:
        print(number)


#password generator project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


#Easy level
password_list = []

for letter in range(0,nr_letters):
    password_list += random.choice(letters)

for symbol in range(0,nr_symbols):
    password_list += random.choice(symbols)

for number in range(0,nr_numbers):
    password_list += random.choice(numbers)

print(password_list)
# char_password = list(password)
# # pass_len = len(char_password)
# # new_password = ''
# # for char in range (0,pass_len):
# #     new_password += random.shuffle(password)
# # print(pass_len)
# random.shuffle(char_password)
# print(char_password)
#
# print(''.join(char_password))

random.shuffle(password_list)
print(password_list)
password = ''
for char in password_list:
    password+= char
print("your final password is",password)
