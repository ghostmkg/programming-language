import java.util.HashMap;

class TrieNode {
    // HashMap to store children of the node (for each character)
    HashMap<Character, TrieNode> children;
    // Boolean flag to mark the end of a word
    boolean isEndOfWord;

    // Constructor
    public TrieNode() {
        children = new HashMap<>();
        isEndOfWord = false;
    }
}

class Trie {
    private TrieNode root;

    // Constructor to initialize the root node
    public Trie() {
        root = new TrieNode();
    }

    // Method to insert a word into the Trie
    public void insert(String word) {
        TrieNode current = root;
        for (char c : word.toCharArray()) {
            // If the character is not already in the children, add it
            current.children.putIfAbsent(c, new TrieNode());
            // Move to the child node
            current = current.children.get(c);
        }
        // Mark the end of the word
        current.isEndOfWord = true;
    }

    // Method to search for a word in the Trie
    public boolean search(String word) {
        TrieNode current = root;
        for (char c : word.toCharArray()) {
            // If the character is not found in the children, return false
            if (!current.children.containsKey(c)) {
                return false;
            }
            // Move to the child node
            current = current.children.get(c);
        }
        // Return true if it's the end of a valid word
        return current.isEndOfWord;
    }

    // Optional: Method to check if a prefix exists in the Trie
    public boolean startsWith(String prefix) {
        TrieNode current = root;
        for (char c : prefix.toCharArray()) {
            if (!current.children.containsKey(c)) {
                return false;
            }
            current = current.children.get(c);
        }
        return true;
    }
}

public class TrieExample {
    public static void main(String[] args) {
        Trie trie = new Trie();

        // Insert words into the Trie
        trie.insert("apple");
        trie.insert("app");

        // Search for words
        System.out.println(trie.search("apple"));  // Output: true
        System.out.println(trie.search("app"));    // Output: true
        System.out.println(trie.search("appl"));   // Output: false
        System.out.println(trie.search("banana")); // Output: false

        // Check for prefixes
        System.out.println(trie.startsWith("app")); // Output: true
        System.out.println(trie.startsWith("ban")); // Output: false
    }
}
