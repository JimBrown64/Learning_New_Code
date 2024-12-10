public class App {
    public static void main(String[] args){
        DataBaseConnection connection = new DataBaseConnection();
        connection.connect();
        String result = connection.query("SELECT * FROM Frame;");
        // System.out.println(result);
        UserInterface UI = new UserInterface();
        UI.createWindow(result);
    }
}
