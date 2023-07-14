import mysql.connector
from mysql.connector import Error

# Check if the form is submitted
if request.method == "POST":
    # Retrieve the form data
    name = request.form["name"]
    email = request.form["email"]
    location = request.form["location"]
    college = request.form["college"]
    major = request.form["major"]
    career = request.form["career"]
    dream_company = request.form["dreamCompany"]
    linkedin = request.form["linkedin"]
    projects = request.form["projects"]

    # Validate the form data (you can add your own validation logic here)

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host="localhost",
            user="your_username",
            password="your_password",
            database="your_database_name"
        )

        if connection.is_connected():
            # Prepare and execute the SQL statement
            cursor = connection.cursor()
            sql = "INSERT INTO profiles (name, email, location, college, major, career, dream_company, linkedin, projects) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (name, email, location, college, major, career, dream_company, linkedin, projects)
            cursor.execute(sql, values)

            # Commit the changes
            connection.commit()

            # Check if the data is inserted successfully
            if cursor.rowcount > 0:
                print("Profile created successfully!")
            else:
                print("Error creating profile.")

            # Close the cursor and connection
            cursor.close()
            connection.close()

    except Error as e:
        print("Error connecting to the database:", e)
