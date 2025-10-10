import java.io.*;
import java.net.*;
import java.util.*;
import java.util.concurrent.atomic.AtomicInteger;

public class ChatServer {
    private static final int PORT = 12348;
    private static final Set<ClientHandler> clients = new HashSet<>();

    // ANSI color codes
    private static final String RESET  = "\u001B[0m";
    private static final String[] COLORS = {
            "\u001B[31m", // RED
            "\u001B[32m", // GREEN
            "\u001B[33m", // YELLOW
            "\u001B[34m", // BLUE
            "\u001B[35m", // PURPLE
            "\u001B[36m", // CYAN
            "\u001B[37m"  // WHITE
    };
    private static final AtomicInteger colorIndex = new AtomicInteger(0);

    public static void main(String[] args) {
        System.out.println("Chat server has started on port " + PORT + "...");
        try (ServerSocket serverSocket = new ServerSocket(PORT)) {
            while (true) {
                Socket socket = serverSocket.accept();
                ClientHandler handler = new ClientHandler(socket);
                synchronized (clients) {
                    clients.add(handler);
                }
                handler.start();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static class ClientHandler extends Thread {
        private final Socket socket;
        private PrintWriter out;
        private BufferedReader in;
        private String name;
        private final String color; // assigned color for both name and messages

        ClientHandler(Socket socket) {
            this.socket = socket;
            this.color = COLORS[colorIndex.getAndUpdate(i -> (i + 1) % COLORS.length)];
        }

        @Override
        public void run() {
            try {
                in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                out = new PrintWriter(socket.getOutputStream(), true);

                // Ask for name
                out.println("Enter your name: ");
                name = in.readLine();
                if (name == null || name.trim().isEmpty()) {
                    name = "Anonymous";
                }

                // Announce join (colored)
                broadcast("🔔 " + color + name + RESET + " has joined the chat.");

                String message;
                while ((message = in.readLine()) != null) {
                    // Broadcast colored message: color applies to both name and message text
                    broadcast(color + name + RESET + ": " + color + message + RESET);
                    System.out.println(name + ": " + message); // server log (optional)
                }
            } catch (IOException e) {
                // client disconnected unexpectedly
            } finally {
                // clean up
                try { socket.close(); } catch (IOException ignored) {}
                synchronized (clients) {
                    clients.remove(this);
                }
                broadcast("❌ " + color + name + RESET + " has left the chat.");
            }
        }

        private void broadcast(String msg) {
            synchronized (clients) {
                for (ClientHandler c : clients) {
                    c.out.println(msg);
                }
            }
        }
    }
}
