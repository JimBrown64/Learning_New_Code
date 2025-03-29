public class App {
    public static void main(String[] args){
        DataBaseConnection connection = new DataBaseConnection();
        connection.connect();
       Object[][] queryResult = connection.query("SELECT * FROM Frame;");
       Object[] testOutput = queryResult[1];
       Object testRow = testOutput[0];
        System.out.println("this is the test: " +testRow.toString());
        // UserInterface UI = new UserInterface();
        // UI.createWindow("trying out a table");
        // UI.createTable(queryResult);
    }
}
