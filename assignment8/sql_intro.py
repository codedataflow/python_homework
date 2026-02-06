import sqlite3

with  sqlite3.connect("../db/magazines.db") as conn:
    print("Database created and connected successfully.")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Create tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_name TEXT NOT NULL UNIQUE,
        publisher_id INTEGER NOT NULL,
        FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL,
        subscriber_address TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS subscriptions (
        subscriber_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        expiration_date TEXT NOT NULL,
        PRIMARY KEY (subscriber_id, magazine_id),
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers(subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines(magazine_id)
    )
    """)

    print("Tables created successfully.")

    conn.commit() 
    print("Sample data inserted successfully.")

def add_publisher(cursor, name):
    try:
        cursor.execute(
            "INSERT INTO Publishers (name) VALUES (?)",
            (name,)
        )
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' is already in the database.")

def add_magazine(cursor, magazine_name, publisher_id):
    try:
        cursor.execute(
            "INSERT INTO Magazines (magazine_name, publisher_id) VALUES (?,?)",
            (magazine_name, publisher_id)
        )
    except sqlite3.IntegrityError:
        print(f"Magazine '{magazine_name}' is already in the database or publisher does not exist.")

def add_subscriber(cursor, name, address):

    cursor.execute(
        """
        SELECT * FROM Subscribers 
        WHERE subscriber_name = ? AND subscriber_address = ?
        """,
        (name, address)
    )

    results = cursor.fetchall()

    if len(results) > 0:
        print(f"Subscriber '{name}' at '{address}' is already in the database.")
        return

    try:
        cursor.execute(
            "INSERT INTO Subscribers (subscriber_name, subscriber_address) VALUES (?,?)",
            (name, address)
        )
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute(
            """
            INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?,?,?)
            """,
            (subscriber_id, magazine_id, expiration_date)
        )
    except sqlite3.IntegrityError:
        print(f"Subscription for subscriber {subscriber_id} and magazine {magazine_id} already exists.")

def subscribe_person(cursor, subscriber_name, subscriber_address, magazine_name, expiration_date):

    cursor.execute(
        """
        SELECT subscriber_id 
        FROM Subscribers 
        WHERE subscriber_name = ? AND subscriber_address = ?
        """,
        (subscriber_name, subscriber_address)
    )
    results = cursor.fetchall()

    if len(results) == 0:
        print(f"There was no subscriber named {subscriber_name} at {subscriber_address}.")
        return

    subscriber_id = results[0][0]

    cursor.execute(
        "SELECT magazine_id FROM Magazines WHERE magazine_name = ?",
        (magazine_name,)
    )
    results = cursor.fetchall()

    if len(results) == 0:
        print(f"There was no magazine named {magazine_name}.")
        return

    magazine_id = results[0][0]

    add_subscription(cursor, subscriber_id, magazine_id, expiration_date)

with sqlite3.connect("../db/magazines.db") as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    add_publisher(cursor, "Penguin Random House")
    add_publisher(cursor, "Forbes Media")
    add_publisher(cursor, "National Geographic Partners")

    add_magazine(cursor, "National Geographic", 3)
    add_magazine(cursor, "Forbes", 2)
    add_magazine(cursor, "Vogue", 1)

    add_subscriber(cursor, "Alice Johnson", "12 Maple Street")
    add_subscriber(cursor, "Brian Smith", "45 Oak Avenue")
    add_subscriber(cursor, "Alice Johnson", "78 Pine Road")  # allowed

    add_subscription(cursor, 1, 1, "2025-12-31")
    add_subscription(cursor, 2, 2, "2025-11-30")
    add_subscription(cursor, 3, 1, "2026-01-15")

    conn.commit()
    print("Sample data inserted successfully.")

    print("\n=== All Subscribers ===")
    cursor.execute("SELECT * FROM Subscribers")
    results = cursor.fetchall()

    for row in results:
        print(row)

print("\n=== All Magazines (sorted by name) ===")
cursor.execute("""
SELECT * 
FROM Magazines
ORDER BY magazine_name
""")

results = cursor.fetchall()
for row in results:
    print(row)

print("\n=== Magazines from Forbes Media ===")

cursor.execute("""
SELECT Magazines.magazine_id,
       Magazines.magazine_name,
       Publishers.name AS publisher_name
FROM Magazines
JOIN Publishers
ON Magazines.publisher_id = Publishers.publisher_id
WHERE Publishers.name = ?
""", ("Forbes Media",))

results = cursor.fetchall()
for row in results:
    print(row)
