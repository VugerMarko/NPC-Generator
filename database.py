import sqlite3

connection = sqlite3.connect("Specifications.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS classes(
        class_name TEXT,
        class_ability TEXT,
        is_spellcaster BOOLEAN
    )               
""")

cursor.execute("""
    INSERT INTO classes VALUES
        ('Cleric', 'WIS', TRUE),
        ('Paladin', 'STR', TRUE),
        ('Barbarian', 'STR', FALSE),
        ('Bard', 'CHA', TRUE),
        ('Druid', 'WIS', TRUE),
        ('Fighter', 'DEX', FALSE),
        ('Monk', 'DEX', FALSE),
        ('Ranger', 'DEX', TRUE),
        ('Rogue', 'DEX', FALSE),
        ('Sorcerer', 'CHA', TRUE),
        ('Warlock', 'CHA', TRUE),
        ('Wizard', 'INT', TRUE)
""")

connection.commit()

connection.close()