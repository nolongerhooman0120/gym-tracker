from db import setup_database
from workout import log_workout, add_exercise, view_all_workouts, update_exercise, delete_workout

def display_workouts(rows):
    if not rows:
        print("\nNo workouts logged yet.")
        return
    current_workout = None
    for row in rows:
        workout_id, date, notes, name, muscle, sets, reps, weight = row
        if workout_id != current_workout:
            print(f"\n{'='*40}")
            print(f"Workout #{workout_id} | {date} | {notes or 'No notes'}")
            print(f"{'='*40}")
            current_workout = workout_id
        if name:
            print(f"  • {name} ({muscle}) — {sets}x{reps} @ {weight}kg")

def main():
    setup_database()

    while True:
        print("\n===== GYM TRACKER =====")
        print("1. Log new workout")
        print("2. Add exercise to a workout")
        print("3. View all workouts")
        print("4. Update an exercise")
        print("5. Delete a workout")
        print("6. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            date = input("Date (YYYY-MM-DD): ").strip()
            notes = input("Notes (optional): ").strip()
            workout_id = log_workout(date, notes)
            print(f"Workout logged! ID: #{workout_id}")

        elif choice == "2":
            workout_id = int(input("Workout ID to add exercise to: "))
            name = input("Exercise name: ").strip()
            muscle = input("Muscle group: ").strip()
            sets = int(input("Sets: "))
            reps = int(input("Reps: "))
            weight = float(input("Weight (kg): "))
            add_exercise(workout_id, name, muscle, sets, reps, weight)
            print("Exercise added!")

        elif choice == "3":
            rows = view_all_workouts()
            display_workouts(rows)

        elif choice == "4":
            exercise_id = int(input("Exercise ID to update: "))
            sets = int(input("New sets: "))
            reps = int(input("New reps: "))
            weight = float(input("New weight (kg): "))
            update_exercise(exercise_id, sets, reps, weight)
            print("Exercise updated!")

        elif choice == "5":
            workout_id = int(input("Workout ID to delete: "))
            delete_workout(workout_id)
            print("Workout deleted.")

        elif choice == "6":
            print("See you at the gym! 💪")
            break

        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()