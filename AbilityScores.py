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
    
    modifiers = []
    
    newSkillList = []
    
    for _ in range(3):
        choice = random.choice(classSkills)
        if choice not in newSkillList:
            newSkillList.append(choice)
    #I dont think this should be working becuase i didnt take ability modifiers for respectable skills i just took out somethingn else
    for index, key in enumerate(ability_dict.items()):
        for skill in skill_dict:
            if key == skill:
                modifier = abiBonus[index] + profiBonus
                modifiers.append(modifier)
                
    print("Character is proficient in:\n")
    for index, skill in enumerate(newSkillList):
        #indexerror: list index out of range
        print(f"{skill} ({modifiers[index]})\n")
    
    return newSkillList

