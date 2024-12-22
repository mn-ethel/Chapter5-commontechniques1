import random
trials=10000
switch_wins = 0
no_switch_wins = 0
for i in range(trials):
        prize_door = random.randint(1, 3)
        contestant_pick = random.randint(1, 3)

        possible_doors = [door for door in [1, 2, 3] if door != prize_door and door != contestant_pick]
        monty_opens = random.choice(possible_doors)
        remaining_doors = [door for door in [1, 2, 3] if door != contestant_pick and door != monty_opens]
        switch_pick = remaining_doors[0]
        if switch_pick == prize_door:
            switch_wins += 1

        if contestant_pick == prize_door:
            no_switch_wins += 1



    switch_percentage = (switch_wins / trials) * 100
no_switch_percentage = (no_switch_wins / trials) * 100

print("Switching wins:",switch_percentage,"% of the time")
print("Not switching wins: ",no_switch_percentage,"% of the time")
