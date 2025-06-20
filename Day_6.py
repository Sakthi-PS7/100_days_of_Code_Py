#Hurdle 1
def square():
    turn_left()
    n=1
    while n<10:
        move()
        n+=1
    turn_right()
    
    
    

def turn_right(n=1):
    if n<3:
        turn_left()
        turn_right(n+1)

start=1       
for n in range(0,4):
    square()
    start+=1

turn_left()
turn_left()
turn_left()



#Hurdle 4

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def movement():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    
while not at_goal():
    while wall_in_front():
        movement()
    move()