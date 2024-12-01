import random

Ability = {"STR": 0, "DEX": 0, "CON": 0, "INT": 0, "WIS": 0, "CHA": 0}

sum = 0
    
for key in Ability:
    value = 1
    
    for tries in range(3):
    
        while value == 1:
            value = random.choice(range(2, 7))


        print(f"value = {value}")
        sum += value  
        print("another roll")
        print(f"sum = {sum}")
    
    Ability[key] = sum
    sum = 0
    print(f"tries = {tries}")
    print("key passed")
    
        


print(Ability)


# class Stats:
    
#     def abilityStat(stats):
#         for ability in stats.keys():
#             diceRoll(stats.values())
        
#         return f"{stats.keys()} == {stats.values()}\n"
    

# obj = Stats()


    