import random
from database import DnDClass

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


def proficiencyBonus(lvl):
    proficiencyRange = range(1, lvl + 1, 4)
    countProficiency = len(proficiencyRange)
    
    bonus = countProficiency + 1
    
    print(f"level: {lvl} \nproficiency bonus: {bonus}\n")
    
    return bonus


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


def calcHitDice(level, hitDiceObj):
    rolls = level - 1
    
    rollsSum = 0
    
    for _ in range(rolls):
        roll = random.randint(2, hitDiceObj)
        rollsSum += roll
              
    hitDiceSum = hitDiceObj + rollsSum
    
    print(f"HP: {hitDiceSum}\n")
    
    return hitDiceSum


def proficientSkills(skillsOfClass, ability_dict, skill_dict, abiBonus, profiBonus):
   
    text = skillsOfClass
    classSkills = [skill.strip() for skill in text.split(",")]
    
    
    newSkillList = random.sample(classSkills, 3)
    
    results = {}
    
    for skill in newSkillList:
        associated_ability = skill_dict.get(skill, None)
        if associated_ability:    
            ability_index = list(ability_dict.keys()).index(associated_ability)

            modifier = abiBonus[ability_index] + profiBonus
            results[skill] = modifier
        else:
            results[skill] = None
    
    
    for skill, modifier in results.items():
        print(f"{skill}: (+{modifier if modifier is not None else 'No associated ability'})")
    
    return newSkillList

