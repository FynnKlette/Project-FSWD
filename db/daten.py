import sqlite3
import os

skript_ordner = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(skript_ordner, "tauschdaten.db")




with sqlite3.connect(db_path) as conn:
    cursor = conn.cursor()


cursor.execute("""
    INSERT OR IGNORE INTO studiengang (studiengang) VALUES 
    ('Wirtschaftsinformatik'), 
    ('Wirtschaftsingenieur/in - Umwelt und Nachhaltigkeit'),
    ('Business Administration'),
    ('Volkswirtschaftslehre'),
    ('Wirtschaftsrecht'),
    ('International Digital Business'),
    ('Internationales Management / Management International'),
    ('Unternehmensgründung und Unternehmensnachfolge')
    
    """)

cursor.execute("""
    INSERT OR IGNORE INTO studienbüro_ma (ma_id, vorname, name, email, password) VALUES 
    (12345678, 'Max', 'Mustermann', 'max.mustermann@hwr-berlin.de', 'password123'),
    (78654321, 'Anna', 'Schmidt', 'anna.schmidt@hwr-berlin.de', 'password456')
    """)


conn.commit()
