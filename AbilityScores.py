import random


def roll_and_calculate_Ability():
    dice = [random.randint(1, 6) for _ in range(4)]
    
    dice = [random.randint(1, 6) if die == 1 else die for die in dice]
    
    dice.remove(min(dice))
    
    return sum(dice)
    
    
    
def abilityBonus(bonus):
    if bonus >= 10:
        abilityBonus = range(10, bonus + 1, 2)
        countBonus = len(abilityBonus)
        
        modifier = countBonus - 1 
    else:
        abilityBonus = range(bonus - 1, 1, 2)
        countBonus = len(abilityBonus)
        
        modifier = countBonus - 1
        
    return modifier

lvl = 0

def proficiencyBonus():
    
    lvl = random.randint(1, 20)
    
    proficiencyRange = range(1, lvl + 1, 4)
    countProficiency = len(proficiencyRange)
    
    bonus = countProficiency * 2
    
    print(f"level: {lvl} \nproficiency bonus: {bonus}\n")
    
    return lvl


def abilityScoreImprovement(key, obj, increment, modifier):
    
    oldModifier = abilityBonus(key[obj])
    
    if obj in key:
        # print(key[obj])
        key[obj] += increment
        newModifier = abilityBonus(key[obj]) 


    for i, num in enumerate(modifier):
        if num == oldModifier:
            modifier.pop(i)
            modifier.insert(i, newModifier)
        
    # print(f"old modifier: {oldModifier}, new modifier: {newModifier}")
         
    return key, modifier
