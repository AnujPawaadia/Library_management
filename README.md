import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;

public class question_1 {
    public static void main(String[] args) {
        Connection connection = null; // Create a connection object and initialize it to null
        Statement statement = null; // Create a statement object and initialize it to null

        try {
            // Connect to the database
            connection = DriverManager.getConnection("jdbc:mysql://localhost:3306/db1", "root", "1234");

            // Create a statement object
            statement = connection.createStatement();

            // Create the employees table
    

                    String createTableSQL = "CREATE TABLE IF NOT EXISTS book (" +
                               "book_id INT AUTO_INCREMENT PRIMARY KEY," +  // Change 'id' to 'book_id'
                            "title VARCHAR(100) NOT NULL," +              // Change 'first_name' to 'title'
    "author VARCHAR(100) NOT NULL," +             // Change 'last_name' to 'author'
    "status VARCHAR(20) NOT NULL," +             // Change 'email' to 'status'
    "section VARCHAR(50)" +                       // Change 'department' to 'section'
    ")";

            int rowsAffected = statement.executeUpdate(createTableSQL);

            if (rowsAffected >= 0) {
                System.out.println("Table created successfully!"); // Print a success message if table is created
            } else {
                System.out.println("Table creation failed."); // Print a failure message if table creation fails
            }
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage()); // Print an error message if an exception occurs
            e.printStackTrace(); // Print the stack trace of the exception
        } finally {
            try {
                if (statement != null) statement.close(); // Close the statement if it's not null
                if (connection != null) connection.close(); // Close the connection if it's not null
            } catch (Exception e) {
                e.printStackTrace(); // Print the stack trace of any exceptions that occur during closing
            }
        }
    }
}
