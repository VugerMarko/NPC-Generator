import random
from openai import OpenAI


client = OpenAI(
    api_key = "api key"
)

npcClass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer"]

npcRace = ["Elf", "Dragonborn", "Dwarf", "Gnome", "Human", "Orc", "Tiefling", "Halfling"]

def createNPC(raceList, classList):
    dndrace = random.choice(raceList)
    dndclass = random.choice(classList)
    
    prompt = f"Describe a {dndrace} npc who is a {dndclass} in Dungeons and Dragons, make a short, engaging description"
    
    response = client.completions.create(
        model="davinci-002",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    
    description = response.choices[0].text.strip()
    
    output = "Race: {} \nClass: {} \nDescription: \n\n {}".format(dndrace, dndclass, description)
    
    return output




print(createNPC(npcRace, npcClass))

