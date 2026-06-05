from db import conn, cursor

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    major TEXT
)
""")

conn.commit()


def get_input(prompt):
    value = input(prompt).strip()
    while value == "":
        print("Input cannot be empty!")
        value = input(prompt).strip()
    return value


def add_student():
    print("\n--- Add Student ---")
    name = get_input("Enter name: ")
    age = get_input("Enter age: ")
    major = get_input("Enter major: ")
    cursor.execute(
        "INSERT INTO students (name, age, major) VALUES (?, ?, ?)",
        (name, age, major)
    )
    conn.commit()

    print("Student added successfully\n")


def view_students():
    print("\n ===Students List===")
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if not rows:
        print("No students found.\n")
        return

    for row in rows:
        print("-------------")
        print("ID   :", row[0])
        print("Name :", row[1])
        print("Age  :", row[2])
        print("Major:", row[3])
    print()


def search_student():
    print("\n--- Search Student ---")
    name = get_input("Enter name: ")

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )
    row = cursor.fetchone()

    if row:
        print("\nStudent Found")
        print("ID   :", row[0])
        print("Name :", row[1])
        print("Age  :", row[2])
        print("Major:", row[3])
    else:
        print("Student not found.")


def delete_student():
    print("\n--- Delete Student ---")
    name = get_input("Enter name: ")

    cursor.execute(
        "DELETE FROM students WHERE name = ?",
        (name,)
    )
    conn.commit()

    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def update_student():
    print("\n - Update Student - ")
    name = get_input("Enter name of student to update: ")

    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )
    row = cursor.fetchone()

    if not row:
        print("Student not found.")
        return

    new_name = get_input("New name: ")
    new_age = get_input("New age: ")
    new_major = get_input("New major: ")

    cursor.execute("""
        UPDATE students
        SET name = ?, age = ?, major = ?
        WHERE name = ?
    """, (new_name, new_age, new_major, name))

    conn.commit()
    print("Student updated successfully!")

