# Flask CRUD Project
# Flask CRUD Project - Employee Management System

This is a simple **Flask web application** for managing employee records, using **MySQL** as the database.  
It allows users to perform basic **CRUD operations** (Create, Read, Update, Delete) on an Employees table.

## Features

- Add new employee records
- View all employees in a table format
- Update employee details (Department & Salary only)
- Delete employee records
- Bootstrap styled user interface
- Proper error handling and flash messages

## Technologies Used

- Python 3
- Flask
- MySQL
- mysql-connector-python
- HTML, CSS, Bootstrap

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/avinash7833/flask_crud_project.git
   cd flask_crud_project



# Create and activate virtual environment (optional but recommended):
-python -m venv venv
-venv\Scripts\activate  # On Windows


# Install dependencies:
-pip install -r requirements.txt


# Set up the MySQL Database:
-Create a database (e.g., employee_db).

-Import the schema.sql file (if you have one) or create the employees table manually.

# Configure database connection:

-Update database.py with your MySQL username, password, host, and database name.

# Run the application:
-python app.py