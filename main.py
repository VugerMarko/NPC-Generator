import random
import openai
from AbilityScores import *
from data import *
from database import DnDClass

openai.api_key = "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"

def createNPC(raceList, classList):
    dndrace = random.choice(raceList)
    dndclass = random.choice(classList)
    
    npcLevel = random.randint(1, 20)
    
    objClass = DnDClass()
    objClass.loadClassName(dndclass)
    
    abilityModifier = []
    
    for key in Ability:
        Ability[key] = roll_and_calculate_Ability()

        ability_Bonus = abilityBonus(Ability[key])
        abilityModifier.append(ability_Bonus)
        
    abilityScoreImprovement(Ability, objClass.classAbility, 2, abilityModifier)
    
    proficiency = proficiencyBonus(npcLevel)
    calcHitDice(npcLevel, objClass.hitDice)
    
    proficientSkills(objClass.classSkills, Ability, skills, abilityModifier, proficiency)

    gender = random.choice(["male", "female"])
    
    prompt = f"make a short description of a {gender} {dndrace} npc who is a {dndclass}, with name on top, key personality traits and physical traits."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": "You are a creative assistant specializing in fantasy character descriptions."},
                {"role": "user", "content": prompt}
            ],
        max_tokens=150,
        temperature=0.7
    )
    
    description = response['choices'][0]['message']['content'].strip()
    
    
    output = "\nRace: {} \nClass: {}\nAbility modifier: {}\nGender: {} \n \n\n{}".format(dndrace, dndclass, objClass.classAbility, gender, description)
    
    for index, (key, value) in enumerate(Ability.items()):
        print(f"{key}: {value} ({abilityModifier[index]})")
    
    return output




print(createNPC(npcRace, npcClass))


