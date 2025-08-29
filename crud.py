# All the functions for Create, Read, Update, and Delete

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Workout, ExerciseTemplate, ExerciseInstance
import datetime


# SQLite database engine. 
engine = create_engine('sqlite:///fitness.db')

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# --- User Functions ---
def get_or_create_user(username):
    """
    Finds a user by username or creates a new one if they don't exist.
    """
    user = session.query(User).filter_by(username=username).first()
    if not user:
        email = f"{username}@example.com"
        print(f"User '{username}' not found. Creating a new user...")
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
    return user

# --- Workout Functions ---
def create_workout(user, name, notes):
    """
    Creates and returns a new workout for a given user.
    """
    new_workout = Workout(name=name, notes=notes, user=user)
    session.add(new_workout)
    session.commit()
    return new_workout

def get_all_workouts(user):
    """
    Returns a list of all workouts for a specific user, ordered by date.
    """
    return session.query(Workout).filter_by(user_id=user.id).order_by(Workout.date.desc()).all()

def get_workout_by_id(workout_id):
    """
    Finds a single workout by its ID.
    """
    return session.query(Workout).filter_by(id=workout_id).one_or_none()

def delete_workout_by_id(workout_id):
    """
    Deletes a workout and all its associated exercises.
    Returns True if deletion was successful, False otherwise.
    """
    workout = session.query(Workout).filter_by(id=workout_id).one_or_none()
    if workout:
        # Cascade delete is handled by the relationship in models.py
        session.delete(workout)
        session.commit()
        return True
    return False

# --- Exercise Functions ---
def get_or_create_exercise_template(name):
    """
    Finds an existing exercise template or creates a new one.
    """
    template = session.query(ExerciseTemplate).filter_by(name=name).first()
    if not template:
        print(f"Exercise '{name}' not found. Creating a new exercise template...")
        template = ExerciseTemplate(name=name)
        session.add(template)
        session.commit()
    return template

def add_exercise_to_workout(workout, template, sets, reps):
    """
    Creates and adds a new exercise instance to a given workout.
    """
    try:
        new_instance = ExerciseInstance(sets=sets, reps=reps, workout=workout, exercise_template=template)
        session.add(new_instance)
        session.commit()
        return new_instance
    except Exception as e:
        print(f"An error occurred while adding exercise: {e}")
        session.rollback()
        return None
