import java.sql.*;
import java.util.ArrayList;
import java.util.List;

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

    public Object[][] query(String inputQuery){
        // StringBuilder outputStart = new StringBuilder("");
        ResultSet results = null;
        ResultSetMetaData metaData = null;
        Object[][] returnObj = null;       
        try{
            Statement statement = connection.createStatement(
                // ResultSet.TYPE_SCROLL_INSENSITIVE,
                // ResultSet.CONCUR_READ_ONLY
            );
            results = statement.executeQuery(inputQuery);
            metaData = results.getMetaData();
            int columnCount = metaData.getColumnCount();
            String[] columnHeaders = new String[columnCount];
            for(int i  = 1; i <= columnCount; i++){ //populate columnNames
                columnHeaders[i-1] = metaData.getColumnName(i);
            }
            // int rowCount = 0;
            // while(results.next()){
            //     rowCount++;
            // }
            // results.beforeFirst();
            
            // Object[][] data = new Object[rowCount][columnCount];
            List<Object[]> dataList = new ArrayList<>();
    
            // System.out.println("debugger");
            while(results.next()){
                // System.out.println("debugger");
                for(int i = 1; i <= columnCount; i++){
                    String[] tempObj = new String[columnCount];
                    tempObj[columnCount-1] = results.getString(i);
                    // System.out.println("this is when its input!" + tempObj[columnCount-1]);
                    dataList.add(new Object[]{tempObj});

                }
            }
            Object[] testRow = dataList.get(0);
            Object testTestRow = testRow[0];
            System.out.println(testRow[0]);
            // System.out.println("debugger");
            Object[][] data = dataList.toArray(new Object[0][0]);
            returnObj = new Object[][]{columnHeaders,data};
        }catch(SQLException e) {
            e.printStackTrace();
        }
        return returnObj;
        // String output = outputStart.toString();
    }
}

