import java.io.*;
import java.net.*;
import java.util.Scanner;

public class ChatClient {
    private static final String SERVER_ADDRESS = "localhost";
    private static final int SERVER_PORT = 12348;

    public static void main(String[] args) {
        try (Socket socket = new Socket(SERVER_ADDRESS, SERVER_PORT);
             PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) {

            Scanner scanner = new Scanner(System.in);

            // Server will first send "Enter your name: "
            String prompt = in.readLine();
            System.out.print(prompt); // show "Enter your name: "
            String name = scanner.nextLine();
            out.println(name);

            // Thread to listen and print server messages (includes ANSI)
            new Thread(() -> {
                String msg;
                try {
                    while ((msg = in.readLine()) != null) {
                        System.out.println(msg);
                    }
                } catch (IOException e) {
                    // connection closed
                }
            }).start();

            // Read user input and send it
            String input;
            while (scanner.hasNextLine()) {
                input = scanner.nextLine();
                out.println(input);
            }

        } catch (IOException e) {
            System.err.println("Unable to connect to server: " + e.getMessage());
        }
    }
}
