import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": "localhost",
    "user": "root",        # change this if your MySQL username is different
    "password": "YOUR_PASSWORD_HERE"
    "database": "gym_tracker"
}

def get_connection():
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except Error as e:
        print(f"Connection error: {e}")
        return None

def setup_database():
    try:
        conn = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"]
        )
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS gym_tracker")
        cursor.execute("USE gym_tracker")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS workouts (
                id INT AUTO_INCREMENT PRIMARY KEY,
                date DATE NOT NULL,
                notes VARCHAR(255)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS exercises (
                id INT AUTO_INCREMENT PRIMARY KEY,
                workout_id INT NOT NULL,
                name VARCHAR(100) NOT NULL,
                muscle_group VARCHAR(50),
                sets INT,
                reps INT,
                weight_kg FLOAT,
                FOREIGN KEY (workout_id) REFERENCES workouts(id) ON DELETE CASCADE
            )
        """)

        conn.commit()
        print("Database ready.")

    except Error as e:
        print(f"Setup error: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    setup_database()