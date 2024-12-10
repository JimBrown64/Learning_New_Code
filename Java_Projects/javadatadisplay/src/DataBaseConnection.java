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

    public String query(String inputQuery){
        StringBuilder outputStart = new StringBuilder("");
        ResultSet results = null;
        ResultSetMetaData metaData = null;
        try{
            Statement statement = connection.createStatement();
            results = statement.executeQuery(inputQuery);
            metaData = results.getMetaData();
            int columnCount = metaData.getColumnCount();

            for(int i  = 1; i <= columnCount; i++){
                outputStart.append(metaData.getColumnName(i) + "\t");
            }
            outputStart.append("\n");
            while(results.next()){
                for(int i = 1; i <= columnCount; i++){
                    outputStart.append(results.getString(i) + "\t");
                }
                outputStart.append("\n");
            }
        }catch(SQLException e) {
            e.printStackTrace();
        }
        String output = outputStart.toString();
        return output;
    }
}

