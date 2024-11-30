import random
import openai
import time
import os

openai.api_key = "openai api key"

npcClass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer"]

npcRace = ["Elf", "Dragonborn", "Dwarf", "Gnome", "Human", "Orc", "Tiefling", "Halfling"]

def createNPC(raceList, classList):
    dndrace = random.choice(raceList)
    dndclass = random.choice(classList)
    
    gender = random.choice(["male", "female"])
    
    prompt = f"make a short description of a {gender} {dndrace} npc who is a {dndclass}, with key personality traits and physical traits."
    
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
    
    # remaining = response.headers.get('X-RateLimit-Remaining')
    # reset_time = response.headers.get('X-RateLimit-Reset')
    
    output = "Race: {} \nClass: {} \nGender: {} \n \n\n{}".format(dndrace, dndclass, gender, description)
    
    return output



print(createNPC(npcRace, npcClass))

