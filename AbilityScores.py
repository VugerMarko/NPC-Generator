import random

Ability = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

sum = 0
    
for key in Ability:
    value = 1
    
    for tries in range(3):
    
        while value == 1:
            value = random.choice(range(2, 7))

        sum += value          
    
    Ability[key] = sum
    sum = 0


for key, value in Ability.items():
    print(f"{key}: {value}")
