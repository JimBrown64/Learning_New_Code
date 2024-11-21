import java.sql.*;

public class DataBaseConnection{
    Connection connection = null;
    // PreparedStatement statement = null;
    // ResultSet resultSet = null;
    
    public void connect(){
        try {
            connection = DriverManager.getConnection("jdbc:sqlite:src/app.db");
        }  catch (SQLException e) {
            e.printStackTrace();
        }finally{
            if(connection != null){
                System.out.println("Connection successful!");
            }    
        }
    }

    public void disconnect(){
        try{
            connection.close();
            System.out.println("Connection closed.");
        }catch(Exception e){
            e.printStackTrace();
        }
    }
}