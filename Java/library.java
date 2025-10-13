import java.io.*;
import java.util.*;

// Book class
class Book implements Serializable {
    private String title;
    private String author;
    private boolean isIssued;

    public Book(String title, String author) {
        this.title = title;
        this.author = author;
        this.isIssued = false;
    }

    public String getTitle() { return title; }
    public String getAuthor() { return author; }
    public boolean isIssued() { return isIssued; }

    public void issueBook() throws Exception {
        if (isIssued) throw new Exception("Book already issued!");
        this.isIssued = true;
    }

    public void returnBook() {
        this.isIssued = false;
    }

    @Override
    public String toString() {
        return title + " by " + author + (isIssued ? " [Issued]" : " [Available]");
    }
}

// Library class
class Library implements Serializable {
    private List<Book> books;
    private Map<String, String> issuedBooks; // bookTitle -> studentName

    public Library() {
        books = new ArrayList<>();
        issuedBooks = new HashMap<>();
    }

    public void addBook(Book book) {
        books.add(book);
    }

    public void showBooks() {
        if (books.isEmpty()) {
            System.out.println("No books in library.");
            return;
        }
        for (Book b : books) {
            System.out.println(b);
        }
    }

    public void issueBook(String title, String student) {
        for (Book b : books) {
            if (b.getTitle().equalsIgnoreCase(title)) {
                try {
                    b.issueBook();
                    issuedBooks.put(title, student);
                    System.out.println("Book issued to " + student);
                } catch (Exception e) {
                    System.out.println("Error: " + e.getMessage());
                }
                return;
            }
        }
        System.out.println("Book not found!");
    }

    public void returnBook(String title) {
        for (Book b : books) {
            if (b.getTitle().equalsIgnoreCase(title)) {
                if (b.isIssued()) {
                    b.returnBook();
                    issuedBooks.remove(title);
                    System.out.println("Book returned successfully!");
                } else {
                    System.out.println("This book was not issued.");
                }
                return;
            }
        }
        System.out.println("Book not found!");
    }
}

// Background thread for auto-saving library data
class AutoSave extends Thread {
    private Library library;
    private String filename;

    public AutoSave(Library library, String filename) {
        this.library = library;
        this.filename = filename;
    }

    public void run() {
        while (true) {
            try {
                saveLibrary();
                Thread.sleep(5000); // autosave every 5 seconds
            } catch (Exception e) {
                System.out.println("AutoSave Error: " + e.getMessage());
            }
        }
    }

    private void saveLibrary() throws IOException {
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(filename))) {
            oos.writeObject(library);
        }
        System.out.println("[AutoSaved library data]");
    }
}

// Main class
public class LibrarySystem {
    private static final String FILE_NAME = "library.dat";

    // Method to load library data
    public static Library loadLibrary() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(FILE_NAME))) {
            return (Library) ois.readObject();
        } catch (Exception e) {
            return new Library(); // new library if no data found
        }
    }

    public static void main(String[] args) {
        Library library = loadLibrary();
        AutoSave autoSave = new AutoSave(library, FILE_NAME);
        autoSave.setDaemon(true); // run in background
        autoSave.start();

        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("\n--- Library Menu ---");
            System.out.println("1. Add Book");
            System.out.println("2. Show Books");
            System.out.println("3. Issue Book");
            System.out.println("4. Return Book");
            System.out.println("5. Exit");
            System.out.print("Enter choice: ");
            int choice = sc.nextInt();
            sc.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter title: ");
                    String title = sc.nextLine();
                    System.out.print("Enter author: ");
                    String author = sc.nextLine();
                    library.addBook(new Book(title, author));
                    break;

                case 2:
                    library.showBooks();
                    break;

                case 3:
                    System.out.print("Enter book title to issue: ");
                    String issueTitle = sc.nextLine();
                    System.out.print("Enter student name: ");
                    String student = sc.nextLine();
                    library.issueBook(issueTitle, student);
                    break;

                case 4:
                    System.out.print("Enter book title to return: ");
                    String returnTitle = sc.nextLine();
                    library.returnBook(returnTitle);
                    break;

                case 5:
                    System.out.println("Exiting...");
                    System.exit(0);

                default:
                    System.out.println("Invalid choice.");
            }
        }
    }
}
