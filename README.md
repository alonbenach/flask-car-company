###### **This README provides a comprehensive guide for setting up and running your project locally. Please read through it carefully before proceeding. Thanks :)**

# Car Company Management System

This is a web application for managing a car company's data, including customers, car models, car ownerships, and more. The application is built using Flask, SQLAlchemy, and a SQLite database.

## Features

- Manage customers, car models, car ownerships, and other features as a database.
- Add, update, and delete records.
- View lists of records and details for individual records.

## Prerequisites

- Python 3.x
- Git

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/alonbenach/flask-car-company.git
   cd flask-car-company
   ```

2. **Create and activate a virtual environment:**

   ##### On Unix or MacOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   ##### On Windows:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

   - In case your system is set to Restricted, you might first have to run the following in your powershell:

   ```powershell
   Set-ExecutionPolicy Unrestricted -Scope CurrentUser
   ```

3. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**

   Initialize the database and run the migrations:

   ```bash
   $env:FLASK_APP = "code/app.py"
   ```

5. **Run the app:**

   ```bash
   flask run
   ```

   The application will be available at http://127.0.0.1:5000.

## Project Structure

- app.py - The main entry point of the application.
- models.py - Contains the SQLAlchemy models for the database.
- routes/ - Contains the route definitions for the Flask application.
- templates/ - Contains the templates for rendering HTML.
- migrations/ - Contains the database migration files.
- requirements.txt - Lists the Python dependencies for the project.

## Running Tests

### Tests are not yet supported for this project.

## Contributing

**DO NOT PUSH DIRECTLY INTO MAIN**

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.

## Contact

If you have any questions or suggestions, please open an issue or contact the project maintainer at [benach@gmail.com].
