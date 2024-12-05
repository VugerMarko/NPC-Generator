import sqlite3
class DnDClass:
    
    def __init__(self, id_num = -1, className="", classAbility="", classSkills = "", spellcaster = True, hitDice = -1):
        self.id_num = id_num
        self.className = className
        self.classAbility = classAbility
        self.classSkills = classSkills
        self.spellcaster = spellcaster
        self.hitDice = hitDice
        self.connection = sqlite3.connect("Specifications.db")
        self.cursor = self.connection.cursor()
        
        
    def loadClassName(self, className):
        self.cursor.execute("""
            SELECT * FROM classes
            WHERE class_name = ?
        """, (className, ))
        
        results = self.cursor.fetchone()
        if results:
            self.id_num = results[0]
            self.className = results[1]
            self.classAbility = results[2]
            self.spellcaster = results[3]
            self.classSkills = results[4]
            self.hitDice = results[5]
        else:
            raise ValueError(f"Class with name {className} not found.")
        


#Testing the database usage
# class1 = DnDClass()

# try:
#     class1.loadClassName('Bard')
#     print(f"ID: {class1.id_num}")
#     print(f"Class Name: {class1.className}")
#     print(f"Class Ability: {class1.classAbility}")
#     print(f"Is Spellcaster: {class1.spellcaster}")
# except ValueError as e:
#     print(e)


#Old code for defining the database, want to keep it in case something happens

# connection = sqlite3.connect("Specifications.db")

# cursor = connection.cursor()

# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS classes(
#         id INTEGER PRIMARY KEY,
#         class_name TEXT,
#         class_ability TEXT,
#         is_spellcaster BOOLEAN
#     )               
# """)

# cursor.execute("""
#     INSERT INTO classes VALUES
#         (1, 'Cleric', 'WIS', TRUE),
#         (2, 'Paladin', 'STR', TRUE),
#         (3, 'Barbarian', 'STR', FALSE),
#         (4, 'Bard', 'CHA', TRUE),
#         (5, 'Druid', 'WIS', TRUE),
#         (6, 'Fighter', 'DEX', FALSE),
#         (7, 'Monk', 'DEX', FALSE),
#         (8, 'Ranger', 'DEX', TRUE),
#         (9, 'Rogue', 'DEX', FALSE),
#         (10, 'Sorcerer', 'CHA', TRUE),
#         (11, 'Warlock', 'CHA', TRUE),
#         (12, 'Wizard', 'INT', TRUE)
# """)

# connection.commit()

# connection.close()