from flask import Flask, render_template, request, redirect, url_for, flash
import database

app = Flask(__name__)
app.secret_key = 'mydevsecret'

# Home - Display all employees
@app.route('/')
def index():
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Employees")
    employees = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', employees=employees)

# Add new employee
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        department = request.form['department']
        salary = request.form['salary']
        joining_date = request.form['joining_date']

        try:
            conn = database.get_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO Employees (Name, Email, Department, Salary, JoiningDate) VALUES (%s, %s, %s, %s, %s)",
                           (name, email, department, salary, joining_date))
            conn.commit()
            flash('Employee added successfully!', 'success')
        except Exception as e:
            flash(f'Error: {str(e)}', 'danger')
        finally:
            cursor.close()
            conn.close()
        return redirect(url_for('index'))
    return render_template('add_employee.html')

# Edit employee
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):
    conn = database.get_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        department = request.form['department']
        salary = request.form['salary']
        cursor.execute("UPDATE Employees SET Department = %s, Salary = %s WHERE EmployeeID = %s",
                       (department, salary, id))
        conn.commit()
        flash('Employee updated successfully!', 'success')
        return redirect(url_for('index'))

    cursor.execute("SELECT * FROM Employees WHERE EmployeeID = %s", (id,))
    employee = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template('edit_employee.html', employee=employee)

# Delete employee
@app.route('/delete/<int:id>')
def delete_employee(id):
    conn = database.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Employees WHERE EmployeeID = %s", (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash('Employee deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
