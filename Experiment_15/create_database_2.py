import sqlite3
# Connect to database (or create it)
conn = sqlite3.connect('student_big_record.db')
# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create students table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS student_big_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    Subject1 TEXT NOT NULL,
                    Mark1 INTEGER NOT NULL, 
                    Subject2 TEXT NOT NULL,
                    Mark2 INTEGER NOT NULL,
                    Subject3 TEXT NOT NULL,
                    Mark3 INTEGER NOT NULL,
                    Subject4 TEXT NOT NULL,
                    Mark4 INTEGER NOT NULL,
                    Subject5 TEXT NOT NULL,
                    Mark5 INTEGER NOT NULL
                )''')

# Commit the changes
conn.commit()

student_big_record = [
    ('ASHUTOSH KUMAR SINGH', 'PWP', 95, 'SS', 95, 'COA', 95, 'ICE', 95, 'DMGT',52),
    ('HARSH VISHALBHAI TRIVEDI', 'PWP', 85, 'SS', 95, 'COA', 95, 'ICE', 95, 'DMGT',52),
    ('VIRAJ PRAKASHBHAI VAGHASIYA', 'PWP', 90, 'SS', 95, 'COA', 95, 'ICE', 95, 'DMGT',52),
    ('SHIVAM ATULKUMAR BHATT', 'PWP', 93, 'SS', 95, 'COA', 95, 'ICE', 95, 'DMGT',52),
    ('DEVENDRASINH DOLATSINH JADEJA','PWP', 75, 'SS', 95, 'COA', 95, 'ICE', 95, 'DMGT',52)
]

# Using executemany to insert multiple records
cursor.executemany('''INSERT INTO student_big_record (Name,Subject1,Mark1,Subject2,Mark2,Subject3,Mark3,Subject4,Mark4,Subject5,Mark5) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', student_big_record)

# Commit the changes
conn.commit()

# Fetch all student records
cursor.execute('SELECT * FROM student_big_record')
rows = cursor.fetchall()
# Display the results
print("All Student Records:")
for row in rows:
    print(row)

cursor.execute('SELECT Enrollment, Subject1, Mark1 FROM student_big_record WHERE Mark1 > 90')
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

# Update Mark1 for Ashutosh kumar (PWP)
cursor.execute('''UPDATE student_big_record SET Mark1 = 98 WHERE Name = 'ASHUTOSH KUMAR SINGH' AND Subject1 = 'PWP' ''')

# Commit the changes
conn.commit()

# Verify the update
cursor.execute('SELECT Name, Mark1 FROM student_big_record WHERE Name = "ASHUTOSH KUMAR SINGH"')
updated_mark = cursor.fetchone()
print(f"\nUpdated Mark1 for {updated_mark[0]}: {updated_mark[1]}")

# Delete a student record (e.g.,DEVENDRASINH DOLATSINH JADEJA )
cursor.execute('''DELETE FROM student_big_record WHERE Name = 'DEVENDRASINH DOLATSINH JADEJA' ''')

# Commit the changes
conn.commit()

# Verify the deletion
cursor.execute('SELECT * FROM student_big_record WHERE Name = "DEVENDRASINH DOLATSINH JADEJA"')
deleted_Name = cursor.fetchone()

if deleted_Name is None:
    print("\nDEVENDRASINH DOLATSINH JADEJA has been successfully deleted.")
    
# Calculate the average Mark
cursor.execute('''SELECT AVG(Mark1) FROM student_big_record''')
avg_mark = cursor.fetchone()[0]

print(f"\nThe average mark of students is: ${avg_mark:.2f}")

print(f"\nEk_3_Saniya_Mamti_16")

conn.close()