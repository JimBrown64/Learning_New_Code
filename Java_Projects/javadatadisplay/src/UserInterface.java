import javax.swing.*;


import java.awt.BorderLayout;
// import java.awt.event.*;
import java.awt.FlowLayout;


public class UserInterface {
    JFrame mainFrame;

    public void createWindow(String title){
        JFrame frame = new JFrame(title);
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        frame.setVisible(true);
        mainFrame = frame;
        // return frame;
    }

    public void createTable(Object[][] inputs){
        
        String[] columnHeaders = (String[]) inputs[0];
        Object[][] data = (Object[][]) inputs[1];
        JTable table = new JTable(data, columnHeaders);
        System.out.println("First Header: " + columnHeaders[0]);
        System.out.println("First data item: " + data[1][0]);
        
        mainFrame.add(new JScrollPane(table), BorderLayout.CENTER);
        // return table;
    }
}

