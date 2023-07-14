import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('profiles.db')
cursor = conn.cursor()

# Create the profiles table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS profiles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        location TEXT,
        college TEXT,
        major TEXT,
        career TEXT,
        dreamCompany TEXT,
        linkedin TEXT,
        projects TEXT
    )
''')

# Check if the form is submitted
if request.method == 'POST':
    name = request.form['name']
    email = request.form['email']
    location = request.form['location']
    college = request.form['college']
    major = request.form['major']
    career = request.form['career']
    dreamCompany = request.form['dreamCompany']
    linkedin = request.form['linkedin']
    projects = request.form['projects']

    # Insert the data into the profiles table
    cursor.execute('''
        INSERT INTO profiles (name, email, location, college, major, career, dreamCompany, linkedin, projects)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (name, email, location, college, major, career, dreamCompany, linkedin, projects))
    
    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()
    
    # Display a success message
    return "Profile created successfully!"
    
# Retrieve the profiles from the database
cursor.execute('SELECT * FROM profiles')
profiles = cursor.fetchall()

# Check if there are profiles available
if profiles:
    # Loop through each profile and display the data
    for profile in profiles:
        name = profile[1]
        email = profile[2]
        location = profile[3]
        college = profile[4]
        major = profile[5]
        career = profile[6]
        dreamCompany = profile[7]
        linkedin = profile[8]
        projects = profile[9]

        # Display the profile data
        print("<div class='profile'>")
        print(f"<h2>{name}</h2>")
        print(f"<p>Email: {email}</p>")
        print(f"<p>Location: {location}</p>")
        print(f"<p>College: {college}</p>")
        print(f"<p>Major: {major}</p>")
        print(f"<p>Career Aspiration: {career}</p>")
        print(f"<p>Dream Company: {dreamCompany}</p>")
        print(f"<p>LinkedIn: <a href='{linkedin}' target='_blank'>{linkedin}</a></p>")
        print(f"<p>Projects: {projects}</p>")
        print("</div>")
else:
    print("No profiles found.")
