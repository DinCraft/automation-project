package org.dincraft;

import javax.swing.JFrame;

public class App {
  public String getGreeting() { return "Hello World!"; }

  public static void main(String[] args) {
    System.out.println(new App().getGreeting());
    JFrame frame = new JFrame();
    frame.setBounds(10, 10, 100, 100);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setVisible(true);
  }
}
