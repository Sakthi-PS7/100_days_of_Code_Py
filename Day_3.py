#If else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height>=120:
    print('Hurray!, you are eligible for the ride')
else:
    print("Sorry!,you are not tall enough :(")

#Modulo
Given_number=int(input("Enter any random number: "))
if Given_number % 2 == 0:
    print("The given number is even")
else:
    print("The number is odd")

#Nesting and elif
math_score = int(input("What is your math score:"))
eng_score = int(input("What is your eng score:"))

if math_score >= 90:
    if eng_score >= 90:
        print("you are good in both subjects")
    else:
        print("you are only good at math")
else:
    if eng_score >= 90:
        print("you are only good at english")
    else:
        print("you are poor in both subjects")

#Multiple if statements
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")

#python pizza

