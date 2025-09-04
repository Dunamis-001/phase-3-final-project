# Fitness Tracker CLI

A command-line application built using Python with SQLAlchemy for logging and managing workout sessions.  
By Alex Nyamai

## Description

The Fitness Tracker CLI is a command-line interface (CLI) application designed to help users manage their personal workout routines more efficiently. The system provides simple tools for creating workouts, adding exercises with sets and reps, and viewing a complete history of their fitness activities.

Built with Python and SQLAlchemy ORM for database interaction, it demonstrates best practices in database management and user-friendly CLI navigation.

## Features

- **Workout Management:** Create, view, and delete entire workout sessions.  
- **Exercise Tracking:** Add specific exercises to each workout, including details like sets and reps.  
- **CRUD Operations:** Full Create, Read, and Delete functionality for all workout entries.  
- **Data Persistence:** Uses a lightweight and portable SQLite database to store data.  
- **User-Friendly CLI:** Simple command-line menus for easy navigation.

## Technologies Used

- Python 3.x: Core programming language.  
- SQLAlchemy: ORM for database interaction.  
- SQLite: Embedded database engine.  
- pip: Dependency management.

## Project Structure

fitness-tracker-cli/
├── crud.py # All database operations (CRUD)
├── cli.py # Main CLI application entry point (run this!)
├── models.py # SQLAlchemy models for the database schema
└── README.md # This documentation

## Installation and Setup

### Prerequisites

- Python 3.x or higher  
- pip (Python package manager)

### Installation Process

1. **Save the files**  
Ensure that all three project files (`models.py`, `crud.py`, and `cli.py`) are saved in the same directory.

2. **Install required dependencies**  
The project requires SQLAlchemy. Open your terminal or command prompt, navigate to the project directory, and run:

pip install sqlalchemy

### Run the application

python cli.py


This command will automatically create a new file, `fitness.db`, which is your SQLite database.

## How to Use

### Starting the Application

Run the main script to launch the CLI:

python cli.py


### Main Menu Options

The application provides a main menu with the following options:

- **Log a new workout** – Create a new workout session and add exercises.  
- **View all workouts** – Display a summary of all logged workouts.  
- **View workout details** – Get a detailed breakdown of a specific workout by its ID.  
- **Delete a workout** – Permanently remove a workout from the database.

## Module Overview

### `models.py`

Contains the SQLAlchemy ORM models that define the database schema:

- **Workout** – Records for each workout session.  
- **Exercise** – Records for each exercise within a workout.

### `crud.py`

Contains all the CRUD operations:

- Functions to create, read, and delete workouts and exercises.  
- Handles database session management.

### `cli.py`

The main application entry point with:

- The CLI interface.  
- Menu navigation system.  
- User input handling and prompts.

## Database Schema

### Key Tables

**Workouts Table**

- `id`  
- `name`  
- `notes`  
- `date`

**Exercises Table**

- `id`  
- `name`  
- `sets`  
- `reps`  
- `workout_id`

**Relationship with Workouts**

Each exercise is linked to a workout by `workout_id`.

## API Reference (CRUD Functions)

### Workout Operations

- `create_workout()`  
- `get_all_workouts()`  
- `get_workout_by_id()`  
- `delete_workout_by_id()`

### Exercise Operations

- `add_exercise_to_workout()`  
- `get_exercises_for_workout()`

## Development

### Adding New Features

1. Update models in `models.py` if a new data type is needed.  
2. Add corresponding CRUD functions in `crud.py` for any new operations.  
3. Update CLI logic in `cli.py` to add new menu options or prompts.  
4. Test thoroughly to ensure the new features work as expected.

## Common Issues and Solutions

### Module Import Issues

**Error:** `ModuleNotFoundError: No module named 'sqlalchemy'`  
**Solution:** Ensure you have installed the dependency by running:

pip install sqlalchemy


in your terminal.

## Support and Contact

If you have any questions, suggestions, or need assistance, please contact the author:

Alex Nyamai

## License

MIT License

Copyright © 2025 Alex Nyamai.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 