import sqlite3
connection = sqlite3.connect('basededonnee.db')
with open('donnee.sql') as f:
	connection.executescript(f.read())
cur = connection.cursor()
cur.execute("INSERT INTO Etudiant (Numero, Code, Nom, Prenom, Adresse) VALUES (?, ?, ?, ?, ?)",
('1234567', 'JMLKAZER','Diouf','Moussa','LacRose'))
cur.execute("INSERT INTO Etudiant (Numero, Code, Nom, Prenom, Adresse) VALUES (?, ?, ?, ?, ?)",
('1665566', 'JJDJDNR','Diop','Mame','Dakar')
)

connection.commit()
connection.close()
