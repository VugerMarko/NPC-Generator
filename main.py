import random
import openai

npcClass = ["Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin", "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard", "Artificer"]

npcRace = ["Elf", "Dragonborn", "Dwarf", "Gnome", "Human", "Orc", "Tiefling", "Halfling"]

def createNPC(raceList, classList):
    dndrace = random.choice(raceList)
    dndclass = random.choice(classList)
    
    output = "Race: {} \nClass: {} \n".format(dndrace, dndclass)
    
    return output


print(createNPC(npcRace, npcClass))

