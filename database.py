import sqlite3

connection = sqlite3.connect("Specifications.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes(
        class_name TEXT,
        class_ability TEXT
    )               
""")

cursor.execute("""
    INSERT INTO classes VALUES
        ('Cleric', 'WIS'),
        ('Paladin', 'STR'),
        ('Barbarian', 'STR'),
        ('Bard', 'CHA'),
        ('Druid', 'WIS'),
        ('Fighter', 'DEX'),
        ('Monk', 'DEX'),
        ('Ranger', 'DEX'),
        ('Rogue', 'DEX'),
        ('Sorcerer', 'CHA'),
        ('Warlock', 'CHA'),
        ('Wizard', 'INT')
""")

connection.commit()

connection.close()