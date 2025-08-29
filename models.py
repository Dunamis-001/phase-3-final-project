


import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

# The base class that models will inherit from
Base = declarative_base()

# Define the User class
class User(Base):
    """
    Represents a user in the fitness tracker.
    A user can have many workouts.
    """
    __tablename__ = 'users'

    # Columns
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)

    # Relationship to Workout
    workouts = relationship('Workout', back_populates='user')

    def __str__(self):
        return f"<User(username='{self.username}', email='{self.email}')>"

# Define the Workout class
class Workout(Base):
    """
    Represents a workout session.
    A workout belongs to a single user and can have many exercises.
    """
    __tablename__ = 'workouts'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    date = Column(Date, default=datetime.date.today)
    notes = Column(String)

    # Foreign key for the one-to-many relationship with User
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships to User and ExerciseInstance
    user = relationship('User', back_populates='workouts')
    exercise_instances = relationship('ExerciseInstance', back_populates='workout', cascade="all, delete, delete-orphan")

    def __str__(self):
        return f"<Workout(name='{self.name}', date='{self.date}', user_id={self.user_id})>"

# Define the ExerciseTemplate class to avoid data duplication
class ExerciseTemplate(Base):
    """
    Represents a generic exercise type (e.g., "Squats").
    This table stores a list of unique exercises.
    """
    __tablename__ = 'exercise_templates'

    # Columns
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)

    # Relationship to ExerciseInstance
    exercise_instances = relationship('ExerciseInstance', back_populates='exercise_template')

    def __str__(self):
        return f"<ExerciseTemplate(name='{self.name}')>"

# Define the ExerciseInstance class to represent an exercise within a workout
class ExerciseInstance(Base):
    """
    Represents an exercise within a workout, with a link to its template.
    Each instance belongs to a single workout and a single exercise template.
    """
    __tablename__ = 'exercise_instances'

    # Columns
    id = Column(Integer, primary_key=True)
    sets = Column(Integer)
    reps = Column(Integer)
    
    # Foreign key for the one-to-many relationship with Workout
    workout_id = Column(Integer, ForeignKey('workouts.id'))
    
    # Foreign key for the many-to-one relationship with ExerciseTemplate
    exercise_template_id = Column(Integer, ForeignKey('exercise_templates.id'))

    # Relationships
    workout = relationship('Workout', back_populates='exercise_instances')
    exercise_template = relationship('ExerciseTemplate', back_populates='exercise_instances')

    def __str__(self):
        return f"<ExerciseInstance(sets={self.sets}, reps={self.reps}, workout_id={self.workout_id}, template_id={self.exercise_template_id})>"
