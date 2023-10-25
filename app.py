
from flask import Flask, render_template, request, abort
import mysql.connector

app = Flask(__name__)

# Configure your MySQL database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Meenaranga@8746",
    database="users"
)

# Task 1: Flask API Development
@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/users')
def users():
    cursor = db.cursor()
    cursor.execute("SELECT id, name, email, role FROM users")
    users_data = cursor.fetchall()
    return render_template('users.html', users=users_data)

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'GET':
        return render_template('new_user_form.html')
    elif request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        role = request.form['role']

        cursor = db.cursor()
        query = "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, role))
        db.commit()

        return "User added successfully!"

@app.route('/users/<int:id>')
def get_user(id):
    cursor = db.cursor()
    query = "SELECT id, name, email, role FROM users WHERE id = %s"
    cursor.execute(query, (id,))
    user_data = cursor.fetchone()

    if user_data:
        return f"User ID: {user_data[0]}, Name: {user_data[1]}, Email: {user_data[2]}, Role: {user_data[3]}"
    else:
        abort(404)  # Raise a 404 Not Found error if the user is not found

# Error handling
@app.errorhandler(404)
def page_not_found(error):
    return "404 - User not found", 404

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)