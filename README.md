
Fitness Tracker CLI

This project is a command-line application designed to help users log and manage their workout sessions and exercises. It allows users to track their progress, view workout history, and maintain a personal log of their fitness activities.

Table of Contents
Features

Technologies Used

Project Structure

Setup Instructions

How to Run

Usage

License

Features
Log New Workouts: Easily record new workout sessions with a name and notes.

Track Exercises: Add specific exercises to each workout, including sets and reps.

View Workout History: Display a list of all past workouts, each identified by a unique ID.

View Detailed Workouts: Get a detailed breakdown of a specific workout, including all logged exercises.

Delete Workouts: Permanently remove a workout and its associated exercises from the database.

Technologies Used
Python: The core programming language for the entire application.

SQLAlchemy: An Object-Relational Mapper (ORM) used to interact with the database.

SQLite: A lightweight, file-based database that stores all workout data.

Project Structure
fitness-tracker-cli/
├── models.py      <-- Defines the database schema for workouts and exercises
├── crud.py        <-- Contains all the database operations (Create, Read, Update, Delete)
├── cli.py         <-- The main file for the command-line interface and user interaction
└── fitness.db     <-- (Automatically generated after first run) The SQLite database file

Setup Instructions
Follow these steps to get the project running on your local machine.

Prerequisites
Python 3.x: Ensure you have Python installed on your system. You can check by running python --version or python3 --version in your terminal.

pip: The Python package installer.

Install Dependencies
This project requires SQLAlchemy. Open your terminal and run the following command to install it:

pip install sqlalchemy

How to Run
Open your terminal or command prompt.

Navigate to the directory where you saved models.py, crud.py, and cli.py.

Run the main application file:

python cli.py

Usage
When the application starts, it will prompt you for a username. This will create a new user profile or load an existing one.

Log a new workout: Select option 1 from the main menu. You will be guided to enter the workout name, notes, and exercises.

View all workouts: Select option 2 to see a summary of all workouts you've logged.

View workout details: Select option 3 and enter the ID of a specific workout to see its exercises.

Delete a workout: Select option 4 and enter the ID of the workout you wish to delete.

License
MIT License
Copyright © 2025 Alex Nyamai.
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.