import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

public class DatabaseExample {
    // Database credentials
    static final String DB_URL = "jdbc:mysql://localhost:3306/unitedsacco"; // Replace with your database name
    static final String USER = "root";  // Replace with your MySQL username
    static final String PASS = "databaseproject";      // Replace with your MySQL password

    public static void main(String[] args) {
        try {
            // 1. Load MySQL JDBC Driver
            Class.forName("com.mysql.cj.jdbc.Driver");

            // 2. Establish a connection
            Connection conn = DriverManager.getConnection(DB_URL, USER, PASS);
            System.out.println("Connected to database successfully!");

            // 3. Create a table
            createTable(conn);

            // 4. Insert user details
            insertData(conn);

            // 5. Close connection
            conn.close();
            System.out.println("Connection closed.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    // Function to create a table
    public static void createTable(Connection conn) throws SQLException {
        String createTableSQL = "CREATE TABLE IF NOT EXISTS members2 (" +
                                "id INT AUTO_INCREMENT PRIMARY KEY, " +
                                "name VARCHAR(100), " +
                                "email VARCHAR(100), " +
                                "phone VARCHAR(15))";
        PreparedStatement stmt = conn.prepareStatement(createTableSQL);
        stmt.executeUpdate();
        System.out.println("Table 'members' created successfully.");
    }

    // Function to insert user data into the table
    public static void insertData(Connection conn) throws SQLException {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter Name: ");
        String name = scanner.nextLine();

        System.out.print("Enter Email: ");
        String email = scanner.nextLine();

        System.out.print("Enter Phone Number: ");
        String phone = scanner.nextLine();

        String insertSQL = "INSERT INTO members (name, email, phone) VALUES (?, ?, ?)";
        PreparedStatement stmt = conn.prepareStatement(insertSQL);
        stmt.setString(1, name);
        stmt.setString(2, email);
        stmt.setString(3, phone);

        int rowsInserted = stmt.executeUpdate();
        if (rowsInserted > 0) {
            System.out.println("User details inserted successfully!");
        }

        scanner.close();
    }
}
