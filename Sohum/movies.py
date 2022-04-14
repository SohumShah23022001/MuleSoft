import sqlite3

# Connect to the database (new/existing)
db = sqlite3.connect('mydb.db')
cursor = db.cursor()

movies = [
    {'title': 'Interstellar', 'year': 2014, 'director': 'Christopher Nolan', 'actor': 'Matthew McConaughey', 'actress': 'Anne Hathaway'},
    {'title': 'Avatar', 'year': 2009, 'director': 'James Cameron', 'actor': 'Sam Worthington', 'actress': 'Zoe Saldana'},
    {'title': 'The Dark Knight', 'year': 2008, 'director': 'Christopher Nolan', 'actor': 'Christian Bale', 'actress': 'Heath Ledger'},
    {'title': 'Avengers: Infinity War', 'year': 2018, 'director': 'Anthony Russo', 'actor': 'Robert Downey Jr', 'actress': 'Chrissie Smith'},
    {'title': 'Iron Man 3', 'year': 2013, 'director': 'Shane Black', 'actor': 'Robert Downey Jr', 'actress': 'Gwyneth Paltrow'}
]

# Creating table 'Movies'
cursor.execute("CREATE TABLE Movies (title VARCHAR(60), actor VARCHAR(24), actress VARCHAR(24), year INT(4), director VARCHAR(24));")

# Inserting data into the table
for movie in movies:
    cursor.execute(f"INSERT INTO Movies VALUES (\'{movie['title']}\', \'{movie['actor']}\', \'{movie['actress']}\', {movie['year']}, \'{movie['director']}\');")

# Select all movies
print("\nSelect all movies:")
cursor.execute("SELECT * FROM Movies;")
for i in cursor.fetchall():
    print(i)
print("\n")

# Select all movies with the actor 'Robert Downey Jr'
print("Select all movies with the actor 'Robert Downey Jr':")
cursor.execute("SELECT title, year, director FROM Movies WHERE actor='Robert Downey Jr';")
for i in cursor.fetchall():
    print(i)
print("\n")
