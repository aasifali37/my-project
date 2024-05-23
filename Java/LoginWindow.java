import javax.swing.*;
import java.awt.event.*;

public class LoginWindow extends JFrame implements ActionListener {
    JTextField usernameField;
    JPasswordField passwordField;
    JButton loginButton;
    
    public LoginWindow() {
        // Set window title
        setTitle("Login Window");
        
        // Create username label and text field
        JLabel usernameLabel = new JLabel("Username:");
        usernameField = new JTextField(20);
        
        // Create password label and password field
        JLabel passwordLabel = new JLabel("Password:");
        passwordField = new JPasswordField(20);
        
        // Create login button
        loginButton = new JButton("Login");
        loginButton.addActionListener(this);
        
        // Create panel to hold components
        JPanel panel = new JPanel();
        panel.add(usernameLabel);
        panel.add(usernameField);
        panel.add(passwordLabel);
        panel.add(passwordField);
        panel.add(loginButton);
        
        // Add panel to the frame
        add(panel);
        
        // Set frame size and visibility
        setSize(300, 250);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }
    
    public void actionPerformed(ActionEvent e) {
        // Check if login button is clicked
        if (e.getSource() == loginButton) {
            // Get username and password from text fields
            String username = usernameField.getText();
            String password = new String(passwordField.getPassword());
            
            // Check if username and password are valid
            if (username.equals("admin") && password.equals("password")) {
                JOptionPane.showMessageDialog(this, "Login successful!");
            } else {
                JOptionPane.showMessageDialog(this, "Invalid username or password. Please try again.");
            }
        }
    }
    
    public static void main(String[] args) {
        new LoginWindow();
    }
}
