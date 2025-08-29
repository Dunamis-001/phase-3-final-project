# contains the Command Line Interface (CLI) logic.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
import crud


engine = create_engine('sqlite:///fitness.db')


def print_menu():
    """
    Displays the main menu options to the user.
    """
    print("\n--- Fitness Tracker CLI ---")
    print("1. Log a new workout")
    print("2. View all past workouts")
    print("3. View details of a specific workout")
    print("4. Delete a workout")
    print("5. Exit")

def print_workout_summary(workout):
    """
    Prints a formatted summary of a single workout.
    """
    print(f"\nWorkout ID: {workout.id}")
    print(f"Name: {workout.name}")
    print(f"Date: {workout.date.strftime('%Y-%m-%d')}")
    if workout.notes:
        print(f"Notes: {workout.notes}")
    print("-------------------------")

# --- CLI Core Functions ---
def log_new_workout(user):
    """
    Guides the user through logging a new workout session.
    """
    print("\n--- Log a New Workout ---")
    name = input("Enter workout name (e.g., 'Leg Day', 'Cardio'): ")
    notes = input("Enter any notes (optional): ")
    
    new_workout = crud.create_workout(user, name, notes)
    
    print(f"Workout '{new_workout.name}' logged successfully with ID: {new_workout.id}.")
    
    # Prompt to add exercises
    add_more = 'y'
    while add_more.lower() == 'y':
        add_exercise_to_workout(new_workout.id)
        add_more = input("Add another exercise to this workout? (y/n): ")

def add_exercise_to_workout(workout_id):
    """
    Adds an exercise instance to a specific workout by referencing a template.
    """
    workout = crud.get_workout_by_id(workout_id)
    if not workout:
        print(f"Error: Workout with ID {workout_id} not found.")
        return

    print(f"\n--- Add Exercise to '{workout.name}' (ID: {workout.id}) ---")
    exercise_name = input("Enter exercise name: ")
    sets_input = input("Enter number of sets: ")
    reps_input = input("Enter number of reps: ")
    
    try:
        sets = int(sets_input)
        reps = int(reps_input)
        
        template = crud.get_or_create_exercise_template(exercise_name)
        
        crud.add_exercise_to_workout(workout, template, sets, reps)
        print(f"Exercise '{exercise_name}' added successfully!")
    except ValueError:
        print("Invalid input for sets or reps. Please enter a number.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_all_workouts(user):
    """
    Fetches and displays a list of all workouts for the current user.
    """
    print("\n--- Your Workout History ---")
    workouts = crud.get_all_workouts(user)
    
    if not workouts:
        print("No workouts found. Log a new one to get started!")
        return

    for workout in workouts:
        print(f"ID: {workout.id} | Date: {workout.date.strftime('%Y-%m-%d')} | Name: {workout.name}")

def view_workout_details():
    """
    Fetches and displays the details of a specific workout, including its exercises.
    """
    try:
        workout_id = int(input("\nEnter the ID of the workout you want to view: "))
        workout = crud.get_workout_by_id(workout_id)
        
        if not workout:
            print(f"No workout found with ID {workout_id}.")
            return

        print_workout_summary(workout)
        
        if not workout.exercise_instances:
            print("No exercises logged for this workout.")
        else:
            print("Exercises:")
            for instance in workout.exercise_instances:
                template_name = instance.exercise_template.name if instance.exercise_template else "Unknown Exercise"
                print(f"  - {template_name}: {instance.sets} sets, {instance.reps} reps")

    except ValueError:
        print("Invalid input. Please enter a number for the workout ID.")
    except Exception:
        print("An error occurred. Please try again.")

def delete_workout():
    """
    Deletes a workout and all its associated exercises.
    """
    try:
        workout_id = int(input("\nEnter the ID of the workout you want to delete: "))
        workout = crud.get_workout_by_id(workout_id)
        
        if not workout:
            print(f"No workout found with ID {workout_id}.")
            return
        
        confirm = input(f"Are you sure you want to delete '{workout.name}'? This action cannot be undone. (y/n): ")
        if confirm.lower() == 'y':
            if crud.delete_workout_by_id(workout_id):
                print(f"Workout with ID {workout_id} deleted successfully.")
            else:
                print("Error: Could not delete workout.")
        else:
            print("Deletion cancelled.")

    except ValueError:
        print("Invalid input. Please enter a number for the workout ID.")
    except Exception:
        print("An error occurred. Please try again.")

# --- Main Application Loop ---
if __name__ == "__main__":
    # For simplicity, we'll assume a single user for this project.
    username = input("Enter your username to begin: ")
    current_user = crud.get_or_create_user(username)
    print(f"Welcome, {current_user.username}!")

    while True:
        print_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            log_new_workout(current_user)
        elif choice == '2':
            view_all_workouts(current_user)
        elif choice == '3':
            view_workout_details()
        elif choice == '4':
            delete_workout()
        elif choice == '5':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")
