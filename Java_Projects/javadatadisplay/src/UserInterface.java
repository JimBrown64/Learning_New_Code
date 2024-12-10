import javax.swing.*;
// import java.awt.event.*;
import java.awt.FlowLayout;

public class UserInterface {


    public JFrame createWindow(String data){
        JFrame frame = new JFrame("Simple UI Example");
        frame.setExtendedState(JFrame.MAXIMIZED_BOTH);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        JTextArea displayData = new JTextArea(data);
        displayData.setEditable(false);

        frame.add(displayData);
        frame.pack();

        frame.setVisible(true);
        return frame;
    }
}

