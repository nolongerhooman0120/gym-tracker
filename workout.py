from db import get_connection

def log_workout(date, notes=""):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO workouts (date, notes) VALUES (%s, %s)", (date, notes))
    conn.commit()
    workout_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return workout_id

def add_exercise(workout_id, name, muscle_group, sets, reps, weight_kg):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO exercises (workout_id, name, muscle_group, sets, reps, weight_kg)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (workout_id, name, muscle_group, sets, reps, weight_kg))
    conn.commit()
    cursor.close()
    conn.close()

def view_all_workouts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT w.id, w.date, w.notes, e.name, e.muscle_group, e.sets, e.reps, e.weight_kg
        FROM workouts w
        LEFT JOIN exercises e ON w.id = e.workout_id
        ORDER BY w.date DESC
    """)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def update_exercise(exercise_id, sets, reps, weight_kg):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE exercises SET sets=%s, reps=%s, weight_kg=%s WHERE id=%s
    """, (sets, reps, weight_kg, exercise_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_workout(workout_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM workouts WHERE id=%s", (workout_id,))
    conn.commit()
    cursor.close()
    conn.close()