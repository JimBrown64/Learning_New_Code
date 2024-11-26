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
        }catch(SQLException e){
            e.printStackTrace();
        }
    }

    public StringBuilder query(String inputQuery){
        StringBuilder output = new StringBuilder("");
        ResultSet results = null;
        ResultSetMetaData metaData = null;
        try{
            Statement statement = connection.createStatement();
            results = statement.executeQuery(inputQuery);
            metaData = results.getMetaData();
            int columnCount = metaData.getColumnCount();

            for(int i  = 1; i <= columnCount; i++){
                output.append(metaData.getColumnName(i) + "\t");
            }
            output.append("\n");
            while(results.next()){
                for(int i = 1; i <= columnCount; i++){
                    output.append(results.getString(i) + "\t");
                }
                output.append("\n");
            }
            System.out.println(output);
        }catch(SQLException e) {
            e.printStackTrace();
        }
        return output;
    }
}

