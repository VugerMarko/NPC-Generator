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


#this function does not work, needs improvement

def abilityScoreImprovement(key, obj):
    if not isinstance(key, dict):
        raise TypeError(f"Expected `key` to be a dictionary, but got {type(key).__name__}.")
    
    if not isinstance(obj, str):
        raise TypeError(f"Expected `obj` to be a string, but got {type(obj).__name__}.")
    
    if obj in key.keys():
        abilityScoreRange = range(1, lvl + 1, 4)
        countAbilityScoreImprovement = len(abilityScoreRange)
        
        abilityImprovement = key.keys() + (countAbilityScoreImprovement * 4)
    else:
        ValueError(f"key value of {key} and {obj} do not match.")
    
    return abilityImprovement
    
    
    

