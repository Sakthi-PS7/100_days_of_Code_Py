#Day 3

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
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
Bill = 0

#small pizza
if size == "S":
    Bill+=15
#medium pizza
elif size == "M":
    Bill+=20
#large pizza
elif size == "L":
    Bill+=25
else:
    print("you entered the wrong value :(")

#pepperoni
if pepperoni == "Y":
    if size =="S":
        Bill+=2
    else:
        Bill+=3

#exta cheese
if extra_cheese == "Y":
    Bill+=1

print(f"Your final bill is: ${Bill}.")

#Logical operators

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45<=age<=55:
        bill = 0
        print("Free ride for aged people")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")

#Treasure Island
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
Entry1 = input("Choose either 'L' or 'R'")
if Entry1 == "L":
    Entry2 = input("Do you wanna 'Swim' or 'wait'")
    if Entry2 == "wait":
        Entry3 = input("Which door, 'red' or 'blue' or 'yellow'")
        if Entry3 == "yellow":
            print('Congrats! you win! :)))')
        elif Entry3 == 'Red':
            print('Burned by fire, game over')
        elif Entry3 == 'Blue':
            print('Eaten by beasts, game over')
        else:
            print('game over')
    else:
        print('Attacked by trout, game over')
else:
    print('Fall into hole, game over')

