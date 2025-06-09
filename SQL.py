import sqlite3
import csv
connect= sqlite3.connect('netflix.db')
cursor= connect.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS netflix_dataset (show_id TEXT PRIMARY KEY, type TEXT , title TEXT, director TEXT, cast TEXT, country TEXT, date_added TEXT, release_year INTEGER, rating TEXT, duration TEXT, listed_in TEXT, description TEXT)")

with open("netflix_dataset.csv", "r",encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        cursor.execute('''
        INSERT OR IGNORE INTO netflix_dataset (
            show_id, type, title, director, cast, country,
            date_added, release_year, rating, duration, listed_in, description
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',(
            row['show_id'],
            row['type'],
            row['title'],
            row['director'],
            row['cast'],
            row['country'],
            row['date_added'],
            int(row['release_year']) if row['release_year'] else None,
            row['rating'],
            row['duration'],
            row['listed_in'],
            row['description']
        ))

connect.commit()
cursor.execute("SELECT COUNT(*) FROM netflix_dataset WHERE director LIKE '%Jan Suter%' AND type ='Movie';")
rows= cursor.fetchall()
for row in rows:
    print(row)
connect.close()

