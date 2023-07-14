from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

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
    dreamCompany = request.form['dreamCompany']
    linkedin = request.form['linkedin']
    projects = request.form['projects']

    # Connect to the database
    conn = sqlite3.connect('profiles.db')
    cursor = conn.cursor()

    # Prepare and execute the SQL statement
    sql = "INSERT INTO profiles (name, email, location, college, major, career, dream_company, linkedin, projects) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"
    values = (name, email, location, college, major, career, dreamCompany, linkedin, projects)
    cursor.execute(sql, values)

    # Commit the changes and close the cursor and connection
    conn.commit()
    cursor.close()
    conn.close()
    return "Profile created successfully!"

@app.route('/profiles')
def profiles():
    # Connect to the database
    conn = sqlite3.connect('profiles.db')
    cursor = conn.cursor()

    # Retrieve the profiles from the database
    cursor.execute("SELECT * FROM profiles")
    profiles = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    return render_template('display_profiles.html', profiles=profiles)

if __name__ == '__main__':
    app.run()
