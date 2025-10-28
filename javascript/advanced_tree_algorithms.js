/**
 * Advanced Tree Algorithms in JavaScript
 * ======================================
 * 
 * Trie (Prefix Tree), AVL Tree, and Tree Traversal utilities
 * for efficient string operations and balanced tree structures.
 * 
 * @author Hacktoberfest 2025 Contributor
 */

// ==================== TRIE DATA STRUCTURE ====================

class TrieNode {
    constructor() {
        this.children = new Map();
        this.isEndOfWord = false;
        this.frequency = 0;
    }
}

class Trie {
    constructor() {
        this.root = new TrieNode();
    }

    /**
     * Insert a word into the trie
     * Time: O(m) where m is word length
     * Space: O(m)
     */
    insert(word) {
        let node = this.root;
        
        for (const char of word) {
            if (!node.children.has(char)) {
                node.children.set(char, new TrieNode());
            }
            node = node.children.get(char);
        }
        
        node.isEndOfWord = true;
        node.frequency++;
    }

    /**
     * Search for a word
     * Time: O(m)
     */
    search(word) {
        let node = this.root;
        
        for (const char of word) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char);
        }
        
        return node.isEndOfWord;
    }

    /**
     * Check if prefix exists
     * Time: O(m)
     */
    startsWith(prefix) {
        let node = this.root;
        
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return false;
            }
            node = node.children.get(char);
        }
        
        return true;
    }

    /**
     * Delete a word from trie
     * Time: O(m)
     */
    delete(word) {
        const deleteHelper = (node, word, index) => {
            if (index === word.length) {
                if (!node.isEndOfWord) return false;
                
                node.isEndOfWord = false;
                node.frequency = 0;
                return node.children.size === 0;
            }
            
            const char = word[index];
            const childNode = node.children.get(char);
            
            if (!childNode) return false;
            
            const shouldDeleteChild = deleteHelper(childNode, word, index + 1);
            
            if (shouldDeleteChild) {
                node.children.delete(char);
                return node.children.size === 0 && !node.isEndOfWord;
            }
            
            return false;
        };
        
        return deleteHelper(this.root, word, 0);
    }

    /**
     * Auto-complete suggestions
     * Time: O(p + n) where p is prefix length, n is number of words
     */
    autoComplete(prefix) {
        let node = this.root;
        
        // Navigate to prefix
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return [];
            }
            node = node.children.get(char);
        }
        
        // Collect all words with this prefix
        const results = [];
        
        const dfs = (currentNode, currentWord) => {
            if (currentNode.isEndOfWord) {
                results.push(currentWord);
            }
            
            for (const [char, childNode] of currentNode.children) {
                dfs(childNode, currentWord + char);
            }
        };
        
        dfs(node, prefix);
        return results;
    }

    /**
     * Count words with given prefix
     * Time: O(p + n)
     */
    countWordsWithPrefix(prefix) {
        let node = this.root;
        
        for (const char of prefix) {
            if (!node.children.has(char)) {
                return 0;
            }
            node = node.children.get(char);
        }
        
        let count = 0;
        
        const countWords = (currentNode) => {
            if (currentNode.isEndOfWord) {
                count += currentNode.frequency;
            }
            
            for (const childNode of currentNode.children.values()) {
                countWords(childNode);
            }
        };
        
        countWords(node);
        return count;
    }

    /**
     * Get longest common prefix
     * Time: O(n * m)
     */
    longestCommonPrefix(words) {
        if (words.length === 0) return "";
        
        let prefix = "";
        let node = this.root;
        
        for (let i = 0; i < words[0].length; i++) {
            const char = words[0][i];
            
            if (!node.children.has(char)) break;
            
            // Check if all words have this character at position i
            if (words.every(word => word[i] === char)) {
                prefix += char;
                node = node.children.get(char);
            } else {
                break;
            }
        }
        
        return prefix;
    }
}

// ==================== AVL TREE ====================

class AVLNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
        this.height = 1;
    }
}

class AVLTree {
    constructor() {
        this.root = null;
    }

    /**
     * Get height of node
     */
    getHeight(node) {
        return node ? node.height : 0;
    }

    /**
     * Get balance factor
     */
    getBalance(node) {
        return node ? this.getHeight(node.left) - this.getHeight(node.right) : 0;
    }

    /**
     * Update height of node
     */
    updateHeight(node) {
        if (node) {
            node.height = 1 + Math.max(this.getHeight(node.left), this.getHeight(node.right));
        }
    }

    /**
     * Right rotation
     */
    rotateRight(y) {
        const x = y.left;
        const T2 = x.right;
        
        x.right = y;
        y.left = T2;
        
        this.updateHeight(y);
        this.updateHeight(x);
        
        return x;
    }

    /**
     * Left rotation
     */
    rotateLeft(x) {
        const y = x.right;
        const T2 = y.left;
        
        y.left = x;
        x.right = T2;
        
        this.updateHeight(x);
        this.updateHeight(y);
        
        return y;
    }

    /**
     * Insert and balance
     * Time: O(log n)
     */
    insert(value) {
        this.root = this._insertNode(this.root, value);
    }

    _insertNode(node, value) {
        // Standard BST insertion
        if (!node) {
            return new AVLNode(value);
        }
        
        if (value < node.value) {
            node.left = this._insertNode(node.left, value);
        } else if (value > node.value) {
            node.right = this._insertNode(node.right, value);
        } else {
            return node; // Duplicate
        }
        
        // Update height
        this.updateHeight(node);
        
        // Get balance factor
        const balance = this.getBalance(node);
        
        // Left Left Case
        if (balance > 1 && value < node.left.value) {
            return this.rotateRight(node);
        }
        
        // Right Right Case
        if (balance < -1 && value > node.right.value) {
            return this.rotateLeft(node);
        }
        
        // Left Right Case
        if (balance > 1 && value > node.left.value) {
            node.left = this.rotateLeft(node.left);
            return this.rotateRight(node);
        }
        
        // Right Left Case
        if (balance < -1 && value < node.right.value) {
            node.right = this.rotateRight(node.right);
            return this.rotateLeft(node);
        }
        
        return node;
    }

    /**
     * In-order traversal
     */
    inOrder(node = this.root, result = []) {
        if (node) {
            this.inOrder(node.left, result);
            result.push(node.value);
            this.inOrder(node.right, result);
        }
        return result;
    }

    /**
     * Check if tree is balanced
     */
    isBalanced(node = this.root) {
        if (!node) return true;
        
        const balance = this.getBalance(node);
        
        return Math.abs(balance) <= 1 &&
               this.isBalanced(node.left) &&
               this.isBalanced(node.right);
    }
}

// ==================== DEMONSTRATIONS ====================

console.log('='.repeat(70));
console.log('ADVANCED TREE ALGORITHMS DEMONSTRATION');
console.log('='.repeat(70));

// Trie Demo
console.log('\n1. TRIE (PREFIX TREE)');
console.log('-'.repeat(70));

const trie = new Trie();
const words = ['apple', 'app', 'application', 'apply', 'banana', 'band'];

console.log('   Inserting words:', words);
words.forEach(word => trie.insert(word));

console.log('   Search "app":', trie.search('app'));
console.log('   Search "appl":', trie.search('appl'));
console.log('   Starts with "app":', trie.startsWith('app'));
console.log('   Auto-complete "app":', trie.autoComplete('app'));
console.log('   Count words with "app":', trie.countWordsWithPrefix('app'));

// AVL Tree Demo
console.log('\n2. AVL TREE (SELF-BALANCING)');
console.log('-'.repeat(70));

const avl = new AVLTree();
const values = [10, 20, 30, 40, 50, 25];

console.log('   Inserting values:', values);
values.forEach(val => avl.insert(val));

console.log('   In-order traversal:', avl.inOrder());
console.log('   Is balanced:', avl.isBalanced());
console.log('   Tree height:', avl.getHeight(avl.root));

console.log('\n' + '='.repeat(70));

module.exports = { Trie, AVLTree };
