# Creating SQLite database table.
# Day to day work and practice.

# Imports, creating database file and creating cursor object.
import sqlite3
db = sqlite3.connect('database_manip.db')
cursor = db.cursor()

# Creating Table if it doesn't exist.
cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming
                (id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)''')

# Creating student list and tuples.
students_data = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

# Inserting student id, names and grades into the database.
cursor.executemany('INSERT INTO python_programming (id, name, grade) VALUES (?, ?, ?)', students_data)

# Selecting all records with a grade between 60 and 80.
cursor.execute('SELECT * FROM python_programming WHERE grade BETWEEN 60 AND 80')
print('\nHere are the student records with grades between 60 and 80 in the following format:')
print('[(ID, name, grade)]\n')
print(cursor.fetchall())

# Updating Carl Davis's grade to 65.
cursor.execute('UPDATE python_programming SET grade = ? WHERE name = ?', (65, 'Carl Davis'))

# Deleting Fredrickson's row.
cursor.execute('DELETE FROM python_programming WHERE name = ?', ('Dennis Fredrickson',))

# Changing the grade of all students with an id greater than 55 to 80.
cursor.execute('UPDATE python_programming SET grade = 80 WHERE id > 55')

# Committing changes and closing the connection.
db.commit()
db.close()
