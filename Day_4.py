#Random Module

import random
import my_module

random_integer = random.randint(0,1)
# print(random_integer)

# print(my_module.thala,my_module.my_hero)

if random_integer == 0:
    print("Heads")
else:
    print("Tails")

#Lists
states_in_India = ["TN", "kerala", "Maharastra", "delhi", "WB"]
print(states_in_India[2])

#Banker Roulette

friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

final_bill = random.choice(friends)
print(final_bill)

final_bill_2=random.randint(0,4)
print(friends[final_bill_2])

#Index Error

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][1])

#Roack, paper, scissors game

play = [rock,paper,scissors]
player = int(input("What do you choose: 0 for Rock, 1 for paper and 2 for scissors:"))
print(play[player])

print('Computer chose')
computer = random.randint(0,2)
print(play[computer])

if player>=3 and player<0:
    print('your entry is invalid, you lose :(')
elif computer == 2 and  player == 0:
    print('You win!!!')
elif player == 2 and computer == 0:
    print('You lose :(')
elif computer > player:
    print('You lose :(')
elif player > computer:
    print('You win!!!')
elif player == computer:
    print('--- Its a Tie ---')
else:
    print('your entry is invalid, you lose :(')