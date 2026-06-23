import sqlite3
import os
import bcrypt

skript_ordner = os.path.dirname(os.path.abspath(__file__))
projekt_hauptordner = os.path.dirname(skript_ordner)
db_path = os.path.join(projekt_hauptordner, "tauschdaten.db")





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

    
    #alte bsp daten passwortt nicht gehasht!!!
    cursor.execute("""
    INSERT OR IGNORE INTO studienbüro_ma (ma_id, vorname, name, email, password) VALUES 
    (12345678, 'Max', 'Mustermann', 'max.mustermann@hwr-berlin.de', 'password123'),
    (78654321, 'Anna', 'Schmidt', 'anna.schmidt@hwr-berlin.de', 'password456')
    """)
   
   
    #passwort testpass123 wird verschlüsselt---> ab jetzt werden Mitarbeiter so eingefügt
    passwortnr3= "Testpass123".encode('utf-8')
    hashdp= bcrypt.hashpw(passwortnr3, bcrypt.gensalt())
     
    cursor.execute("""  
    INSERT or ignore INTO studienbüro_ma (ma_id, vorname, name, email, password)
    VALUES (?,?,?,?,?)
    """, (11111111, 'Noah', 'Namo','noah@hwr-berlin.de', hashdp))



    passwortnr4= "hallo".encode('utf-8')
    hashdp2= bcrypt.hashpw(passwortnr3, bcrypt.gensalt())
     
    cursor.execute("""  
    INSERT or ignore INTO studienbüro_ma (ma_id, vorname, name, email, password)
    VALUES (?,?,?,?,?)
    """, (21212121, 'Peter', 'Parker','p@hwr-berlin.de', hashdp2))


conn.commit()

print("erfolgreich")


