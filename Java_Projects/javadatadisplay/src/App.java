public class App {
    public static void main(String[] args){
        DataBaseConnection connection = new DataBaseConnection();
        connection.connect();
        connection.query("SELECT * FROM Frame;");
    }
}