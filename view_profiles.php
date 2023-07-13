<?php
// Connect to the database
$servername = "localhost";
$username = "your_username";
$password = "your_password";
$dbname = "your_database_name";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check the connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

// Retrieve the profiles from the database
$sql = "SELECT * FROM profiles";
$result = $conn->query($sql);

// Check if there are profiles available
if ($result->num_rows > 0) {
  // Loop through each profile and display the data
  while ($row = $result->fetch_assoc()) {
    $name = $row["name"];
    $email = $row["email"];
    $location = $row["location"];
    $college = $row["college"];
    $major = $row["major"];
    $career = $row["career"];
    $dreamCompany = $row["dream_company"];
    $linkedin = $row["linkedin"];
    $projects = $row["projects"];

    // Display the profile data
    echo "<div class='profile'>";
    echo "<h2>$name</h2>";
    echo "<p>Email: $email</p>";
    echo "<p>Location: $location</p>";
    echo "<p>College: $college</p>";
    echo "<p>Major: $major</p>";
    echo "<p>Career Aspiration: $career</p>";
    echo "<p>Dream Company: $dreamCompany</p>";
    echo "<p>LinkedIn: <a href='$linkedin' target='_blank'>$linkedin</a></p>";
    echo "<p>Projects: $projects</p>";
    echo "</div>";
  }
} else {
  echo "No profiles found.";
}

// Close the database connection
$conn->close();
?>
