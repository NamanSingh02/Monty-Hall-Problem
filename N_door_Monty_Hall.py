# Made by Naman Singh, February 2024
import random

def play_swap(door,n):
    chosen=random.randint(0,n-1)
    door_open=random.randint(1,n-1)
    while(door_open==chosen):
        door_open=random.randint(1,n-1)   
    temp=[x for x in range(n)]
    temp.remove(chosen)
    temp.remove(door_open)
    #swapping the chosen door
    chosen=random.choice(temp)
    if(door[chosen]==1):
        return True #win
    return False
def play_not_swap(door,n):
    chosen=random.randint(0,n-1)
    # no need to open any door because the player will not be swapping anyway
    if(door[chosen]==1):
        return True #win
    return False

def monty_hall(n):
    door=[1]
    for i in range(1,n):
        door.append(0)
    score1=score2=0
    for i in range(1000):
        temp1=play_swap(door,n)
        temp2=play_not_swap(door,n)
        if(temp1):
            score1+=1
        if(temp2):
            score2+=1
    print(f"The Monty Hall Problem with {n} doors is considered")
    print()
    print(f"Given that we will swap doors, out of 1000 trials we will win {score1} times")
    print(f"Given that we will not swap doors, out of 1000 trials we will win {score2} times")

n=3
monty_hall(n)

"""
probability of winning by not swap=1/n
probability of losing by not swap= (n-1)/n =probability of winning by choosing any of the remaining doors
now we open 1 door and show that there is no reward behind it.
Hence this probability is distributed among n-2 doors

probability of winning by choosing any 1 remaining door=(((n-1)/n)/(n-2)) which is always greater than 1/n

Hence winning by swapping is more likely!

"""    
    
            
        



