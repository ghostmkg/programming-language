# Chat Application

## Overview

This chat application is a simple multi-user online chat system implemented in Java using socket programming. It allows multiple users to connect to a central server, send messages, and receive messages from other users in real-time.

## Components

- **ChatServer**: The server class that manages connections from multiple clients, assigns unique user IDs, and broadcasts messages to all connected clients.
- **ChatClient**: The client class that connects to the server, sends messages, and receives messages from other clients.

## Features

- Supports multiple clients chatting simultaneously.
- Each client can send and receive messages.
- The server maintains a list of connected users.

## Implementation Details

### Server Implementation

- **Class**: `ChatServer`
- **Port**: Configured to run on port **12348** (can be changed).
- **Functionality**:
  - Listens for incoming client connections.
  - Manages a set of connected clients and broadcasts messages to all users.
  - Each client is handled in a separate thread to enable simultaneous connections.

### Client Implementation

- **Class**: `ChatClient`
- **Functionality**:
  - Connects to the `ChatServer` using sockets.
  - Sends messages to the server and listens for incoming messages.
  - Simple text-based user interface for message input and display.

## How to Run the Application

### Prerequisites

- Java Development Kit (JDK) installed on your machine.
- IntelliJ IDEA (or any Java IDE) for running the code.

### Running the Chat Server

1. Open the `ChatServer` class in IntelliJ IDEA.
2. Run the `ChatServer` class. You should see the message indicating that the server has started:


-----------------------------------------------------------------------

### Running the Chat Clients

1. Open the `ChatClient` class in IntelliJ IDEA.
2. Create multiple run configurations for the clients (e.g., `ChatClient`, `Client1`, `Client2`).
3. Use the **"Multiple Run"** feature to start all client instances simultaneously or run each client instance one by one.


  **Open Run → Edit Configurations...

    Create a new Application configuration:

    Click + → Application.

    Name: Client1

    Main class: TermInYear.ChatClient (use the selector to find it)

4. After starting the clients, you can send messages from any client and see them received by the others.

## Usage

1. **Chatting**: Each client can type a message and press Enter to send it to the server. The server will broadcast the message to all connected clients.
2. **Exit**: To close a client, simply terminate the client window.

## Testing the Application

- Open multiple client instances and verify that messages are successfully sent and received between users.
- Check the server console for logs of received messages and broadcast actions.

## Troubleshooting

- If you encounter a `java.net.ConnectException: Connection refused`, ensure that the `ChatServer` is running before starting the clients.
- Ensure that the port specified in the server matches the port clients are trying to connect to.

## Conclusion

This chat application serves as a basic example of client-server communication using sockets in Java.
