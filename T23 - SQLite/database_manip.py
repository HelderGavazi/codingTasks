import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('School.db')
cursor = conn.cursor()

# Create the python_programming table
cursor.execute('''
DROP TABLE IF EXISTS python_programming;
''')
cursor.execute('''
CREATE TABLE python_programming (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL
);
''')

# Insert new rows into the python_programming table
students = [
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
]

cursor.executemany('''
INSERT INTO python_programming (id, name, grade)
VALUES (?, ?, ?);
''', students)

# Select all records with a grade between 60 and 80
cursor.execute('''
SELECT * FROM python_programming
WHERE grade BETWEEN 60 AND 80;
''')
rows = cursor.fetchall()
print("Records with grades between 60 and 80:")
for row in rows:
    print(row)

# Change Carl Davis’s grade to 65
cursor.execute('''
UPDATE python_programming
SET grade = 65
WHERE name = 'Carl Davis';
''')

# Delete Dennis Fredrickson’s row
cursor.execute('''
DELETE FROM python_programming
WHERE name = 'Dennis Fredrickson';
''')

# Change the grade of all students with an id greater than 55 to a grade of 80
cursor.execute('''
UPDATE python_programming
SET grade = 80
WHERE id > 55;
''')

# Commit the changes and close the connection
conn.commit()

# Verify the final state of the table
cursor.execute('''
SELECT * FROM python_programming;
''')
final_rows = cursor.fetchall()
print("Final state of the python_programming table:")
for row in final_rows:
    print(row)

conn.close()
