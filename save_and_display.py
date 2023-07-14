import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('profiles.db')
cursor = conn.cursor()

# Create a table to store profiles if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS profiles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    location TEXT,
                    college TEXT,
                    major TEXT,
                    career TEXT,
                    dream_company TEXT,
                    linkedin TEXT,
                    projects TEXT
                )''')
conn.commit()


@app.route('/')
def index():
    return render_template('create_profile.html')


@app.route('/save_profile', methods=['POST'])
def save_profile():
    name = request.form['name']
    email = request.form['email']
    location = request.form['location']
    college = request.form['college']
    major = request.form['major']
    career = request.form['career']
    dream_company = request.form['dreamCompany']
    linkedin = request.form['linkedin']
    projects = request.form['projects']

    # Insert the profile data into the database
    cursor.execute('''INSERT INTO profiles (name, email, location, college, major, career, dream_company, linkedin, projects)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', (name, email, location, college, major, career, dream_company, linkedin, projects))
    conn.commit()

    return 'Profile created successfully!'


@app.route('/display_profiles')
def display_profiles():
    cursor.execute('SELECT * FROM profiles')
    profiles = cursor.fetchall()

    return render_template('display_profiles.html', profiles=profiles)


if __name__ == '__main__':
    app.run(debug=True)
