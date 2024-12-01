import random
import openai
import time
import os

openai.api_key = "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"

npcClass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer"]

npcRace = ["Elf", "Dragonborn", "Dwarf", "Gnome", "Human", "Orc", "Tiefling", "Halfling"]

def createNPC(raceList, classList):
    dndrace = random.choice(raceList)
    dndclass = random.choice(classList)
    
    npcLvl = random.choice([1, 20])
    
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
    
    
    output = "Race: {} \nClass: {} \nGender: {} \n \n\n{}".format(dndrace, dndclass, gender, description)
    
    return output



print(createNPC(npcRace, npcClass))


