# Flask-project

## Table of Contents

- [Project Overview](#project-overview)
  
  - [1: Flask API Development](#1-flask-api-development)
  - [2: Database Interaction](#2-database-interaction)
  - [3: Version Control with Git](#3-version-control-with-git)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Database Configuration](#database-configuration)
  - [Database Schema](#database-schema)
  - [Populating the Database with Sample Data](#populating-the-database-with-sample-data)
- [Steps to Fetch Template](#steps-to-fetch-template)
- [Git Workflow](#git-workflow)
- [Running the Application](#running-the-application)
- [Additional Dependencies and Setup Requirements](#additional-dependencies-and-setup-requirements)
  -[Python Dependencies](#python-dependencies)
  -[MySQL Database](#mysql-database)
  -[Version Control Git](#version-control-git)
- [Contributing](#contributing)

## Project Overview

This project is a demonstration of your skills and knowledge as a Software Engineer in Flask, MySQL, and Git concepts. It includes tasks that simulate real-world scenarios and evaluate your proficiency in these technologies.


## 1: Flask API Development

a. Create a new Flask application.

b. Define a route `/hello` that returns the string "Hello, World!" when accessed.

c. Implement a route `/users` that retrieves a list of users from a MySQL database and displays them as a list in an HTML table.

d. Implement a route `/new_user` to render an HTML page for accepting user input and store the information in the database.

e. Create a route `/users/<id>` that retrieves a specific user's details from the database.

f. Add error handling to handle cases when a user or resource is not found.

## 2: Database Interaction

a. Create a MySQL database with the name "users."

b. Design a table "users" with the following columns:
   - id (int, primary key)
   - name (varchar)
   - email (varchar)
   - role (varchar)

c. Write SQL queries to:
   - Insert sample data into the "users" table.
   - Retrieve all users from the "users" table.
   - Retrieve a specific user by their ID.

## 3: Version Control with Git

a. Initialize a new Git repository for your Flask/Django project.

b. Create a branch named "steptech_assignment."

c. Make necessary commits as you implement the Flask API and database functionality.

d. Push your branch to a remote Git repository.

e. Create a pull request from your branch to the main branch (or master branch) of the repository.


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python installed on your machine.
- MySQL server and client tools.
- Git installed for version control.

### Setup

1. Clone this repository to your local machine:

   bash
   git clone https://github.com/your-username/your-project.git
   

2. Navigate to the project directory:

   bash
   cd your-project
   

3. Install project dependencies:

   bash
   pip install -r requirements.txt
   

## Database Configuration

1. Set up a MySQL database with the name "users."
2. Design a table "users" with the specified columns:
   - id (int, primary key)
   - name (varchar)
   - email (varchar)
   - role (varchar)
3. Use SQL queries to populate the "users" table with sample data.


### Database Schema

The application uses a MySQL database with the following schema:

- Table: users
  - `id` (int, primary key): Unique identifier for each user.
  - `name` (varchar): User's name.
  - `email` (varchar): User's email address.
  - `role` (varchar): User's role or position.

### Populating the Database with Sample Data

To populate the database with sample data, you can use SQL queries to insert records into the `users` table. Here's an example of how to add sample data:

sql
-- Inserting a sample user
INSERT INTO users(name,email,role) VALUES ( 'John','john123@gmail.com','admin'),( 'Mary','mary563@gmail.com','manager'),( 'Jane','jane459@gmail.com','supervisor'),( 'Bob','bob759@gmail.com','clerk'),( 'Harry','harry889@gmail.com','supervisor');

-- Retrieve all users from the table. 
SELECT  * FROM users;

--- Retrieve a specific user by their ID.
SELECT * FROM users WHERE id = 2;

You can run these SQL queries using a MySQL client or by incorporating them into your Flask application, for example, in a script that initializes the database with sample data.

This section provides a clear understanding of the database schema and how to populate it with sample data. Be sure to customize it according to your specific database schema and requirements.
  

## Steps to Fetch Template

To fetch the users.html template in your Flask application, you need to ensure that your Flask application is set up correctly, and the template file is located in the appropriate directory. Here are the general steps to fetch the users.html template:

1. Create a Templates Directory:
   - First, ensure that you have a directory named templates in the same directory as your Flask application script (typically, this is where Flask expects to find template files).

2. Place users.html in the Templates Directory:
   - Save your users.html template in the templates directory.

3. Render users.html from Your Flask Route:
   - In your Flask route, use the render_template function to render the users.html template. For example, if your route is /users, you might have code like this:

   python
   @app.route('/users')
   def users():
       cursor = db.cursor()
       cursor.execute("SELECT id, name, email, role FROM users")
       users_data = cursor.fetchall()
       return render_template('users.html', users=users_data)
   
   Here, render_template('users.html', users=users_data) renders the users.html template and passes the users_data variable to the template, which can be used to populate the HTML.

4. Access the Route in Your Web Browser:
   - Once your Flask application is running, you can access the /users route in your web browser. The route will render and display the content of the users.html template.

Make sure that the users.html template is correctly placed in the templates directory, and the route in your Flask application is set up to render it. The render_template function takes care of fetching and rendering the template for you.


## Git Workflow

This project follows a basic Git workflow to manage code contributions. Here are the key aspects of our workflow:

1. Fork the Repository:
   - If you'd like to contribute to this project, start by forking the repository to your own GitHub account.

2. Clone the Repository:
   - Clone your forked repository to your local development environment using the following command:
     
     git clone https://github.com/your-username/your-project.git
     

3. Create a Feature Branch:
   - Before making any changes, create a new branch for your feature, bug fix, or improvement. Use a descriptive name for your branch.
     
     git checkout -b feature/my-feature
     

4. Commit Your Changes:
   - Make your code changes and commit them to your feature branch. Be sure to provide clear and concise commit messages.
     
     git commit -m "Add new feature: my feature description"
     

5. Push to Your Fork:
   - Push your changes to your forked repository on GitHub.
     
     git push origin feature/my-feature
     
6. Create a Pull Request:
   - Go to the original repository on GitHub and create a pull request from your feature branch to the main branch. Provide a detailed description of your changes.

7. Review and Collaboration:
   - Contributors and maintainers will review your pull request, provide feedback, and discuss any necessary changes. Collaborate to refine the code.

8. Merge Your Contribution:
   - Once your pull request is approved, a project maintainer will merge it into the main branch.
  

## Running the Application

1.To run the Flask application, execute the main script:

bash
python your_flask_script.py

Replace `your_flask_script.py` with the name of your Flask application script.

Make sure to configure the database connection in your Flask script before running the application.

2. Access the following routes:

   - `/hello`: Returns "Hello, World!"
   - `/users`: Retrieves and displays a list of users.
   - `/new_user`: Allows adding new users.
   - `/users/<id>`: Retrieves specific user details.


## Additional Dependencies and Setup Requirements

### Python Dependencies

This project uses specific Python libraries and packages that you need to install. You can install them using `pip`. Run the following command to install the required dependencies:

bash
pip install -r requirements.txt

- Flask: The web framework used for creating the API.
- mysql-connector-python: A MySQL database connector for Python.
- gitpython: A Python library for interacting with Git repositories.

### MySQL Database

This project assumes you have a MySQL database configured. Make sure to provide the following details in your configuration:

- Host: Your MySQL server's host or IP address.
- User: Your MySQL username.
- Password: Your MySQL password.
- Database Name: The name of the MySQL database (e.g., 'users').

### Version Control Git

The project is version-controlled using Git. If you plan to contribute or work with the codebase, you'll need Git installed on your system. You can install Git from the official website: [https://git-scm.com/downloads](https://git-scm.com/downloads).

These additional dependencies and setup requirements are crucial for a successful setup and usage of your Flask application. Customize this section to match your specific project dependencies and instructions.


## Contributing

To contribute to this project, please keep the following guidelines in mind:

- Ensure that your code adheres to our coding standards and conventions.
- Write clear and informative commit messages.
- Respect the existing project structure and organization.
- If you're fixing a bug or adding a new feature, provide tests if applicable.
- Be respectful and collaborative in all communication and interactions within the project.

We welcome contributions from the community and appreciate your effort to improve this project. If you have any questions or need assistance, feel free to reach out.

Thank you for considering contributing to our project!
