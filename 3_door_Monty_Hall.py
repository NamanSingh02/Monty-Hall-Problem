# Made by Naman Singh, February 2024
import random

def play_swap(door):
    chosen=random.randint(0,2)
    door_open=random.randint(1,2)
    while(door_open==chosen):
        door_open=random.randint(1,2)
    
    temp=[0,1,2]
    temp.remove(chosen)
    temp.remove(door_open)
    #swap the chosen door
    chosen=temp[0]
    if(door[chosen]==1):
        return True #win
    return False

def play_not_swap(door):
    chosen=random.randint(0,2)
    if(door[chosen]==1):
        return True #win
    return False


door=[1,0,0]
score1=score2=0
for i in range(1000):
    temp1=play_swap(door)
    temp2=play_not_swap(door)
    if(temp1):
        score1+=1
    if(temp2):
        score2+=1
print(f"The Monty Hall Problem with 3 doors is considered")
print()
print(f"Given that we will swap doors, out of 1000 trials we will win {score1} times")
print(f"Given that we will not swap doors, out of 1000 trials we will win {score2} times")