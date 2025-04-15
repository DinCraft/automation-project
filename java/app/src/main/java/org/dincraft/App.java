package org.dincraft;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Scanner;
import javax.swing.JFrame;

public class App {
  public String getGreeting() {
    return "Hello World!";
  }

  public static void execCmd(String cmd) {
    Runtime rt = Runtime.getRuntime();
    String[] commands = {"python", "C:\\Users\\DinCraft\\Desktop\\Folders\\automation-project\\python\\command.py"};
    Process proc;
    try {
      proc = rt.exec(commands);
      BufferedReader stdInput = new BufferedReader(new InputStreamReader(proc.getInputStream()));
      
      BufferedReader stdError = new BufferedReader(new InputStreamReader(proc.getErrorStream()));
      // Read the output from the command
      System.out.println("Here is the standard output of the command:\n");
      String s = null;
      while ((s = stdInput.readLine()) != null) {
        System.out.println(s);
      }
      // Read any errors from the attempted command
      System.out.println("Here is the standard error of the command (if any):\n");
      while ((s = stdError.readLine()) != null) {
        System.out.println(s);
      }
    } catch (IOException e) {
      e.printStackTrace();
    }

  }

  public static void main(String[] args) {
    System.out.println(System.getProperty("user.dir"));
    System.out.println("Some changes");
    System.out.println("One more change");
    execCmd("");
    System.exit(0);
    JFrame frame = new JFrame();
    frame.setBounds(10, 10, 100, 100);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setVisible(true);
  }
}
