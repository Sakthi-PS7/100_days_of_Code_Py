#Day2

#Data types
print('hello'[-2])
print (123_215_329)
print (True)
print(False)

#Type Error, Checking and conversion
print(type('abc'))
print(type(123))
print(type(123.1))
print(type(True))

Name= input("Enter your name: ")
length_of_name= len(Name)
print("Number of letters in your name: " + str(length_of_name))
print(float(123.766))
print(round(float(123.766),1))

# Mathematical operations
print (3//3*3*(3//3))

#Number Manipulation
bmi = 64 / 1.85 ** 2
bun=round(bmi, 2)
age=30
print(f"I am {age} years old and my bmi is {bun}")

age = 10
print(f"Hi my age is={age}")

# Tip calculator project
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

Final_bill = ((bill+((tip/100*bill)))/people)
print("Your Final bill per person is",round(Final_bill,2))
