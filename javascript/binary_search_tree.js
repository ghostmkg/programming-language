/**
 * Binary Search Tree Implementation in JavaScript
 * ===============================================
 * 
 * Complete BST with insertion, deletion, traversal, and utility operations.
 * Includes balancing check, height calculation, and path finding.
 * 
 * @author Hacktoberfest 2025 Contributor
 */

class TreeNode {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}

class BinarySearchTree {
    constructor() {
        this.root = null;
    }

    /**
     * Insert a value into the BST
     * Time: O(log n) average, O(n) worst
     * Space: O(1)
     */
    insert(value) {
        const newNode = new TreeNode(value);
        
        if (!this.root) {
            this.root = newNode;
            return this;
        }
        
        let current = this.root;
        while (true) {
            if (value === current.value) return undefined; // Duplicate
            
            if (value < current.value) {
                if (!current.left) {
                    current.left = newNode;
                    return this;
                }
                current = current.left;
            } else {
                if (!current.right) {
                    current.right = newNode;
                    return this;
                }
                current = current.right;
            }
        }
    }

    /**
     * Search for a value
     * Time: O(log n) average
     */
    search(value) {
        let current = this.root;
        
        while (current) {
            if (value === current.value) return true;
            if (value < current.value) current = current.left;
            else current = current.right;
        }
        
        return false;
    }

    /**
     * Find minimum value
     */
    findMin(node = this.root) {
        if (!node) return null;
        while (node.left) node = node.left;
        return node.value;
    }

    /**
     * Find maximum value
     */
    findMax(node = this.root) {
        if (!node) return null;
        while (node.right) node = node.right;
        return node.value;
    }

    /**
     * Delete a value from BST
     * Time: O(log n) average
     */
    delete(value) {
        this.root = this._deleteNode(this.root, value);
        return this;
    }

    _deleteNode(node, value) {
        if (!node) return null;
        
        if (value < node.value) {
            node.left = this._deleteNode(node.left, value);
        } else if (value > node.value) {
            node.right = this._deleteNode(node.right, value);
        } else {
            // Node to delete found
            
            // Case 1: Leaf node
            if (!node.left && !node.right) return null;
            
            // Case 2: One child
            if (!node.left) return node.right;
            if (!node.right) return node.left;
            
            // Case 3: Two children
            const minRight = this.findMin(node.right);
            node.value = minRight;
            node.right = this._deleteNode(node.right, minRight);
        }
        
        return node;
    }

    /**
     * In-order traversal (Left-Root-Right)
     * Returns sorted array
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
     * Pre-order traversal (Root-Left-Right)
     */
    preOrder(node = this.root, result = []) {
        if (node) {
            result.push(node.value);
            this.preOrder(node.left, result);
            this.preOrder(node.right, result);
        }
        return result;
    }

    /**
     * Post-order traversal (Left-Right-Root)
     */
    postOrder(node = this.root, result = []) {
        if (node) {
            this.postOrder(node.left, result);
            this.postOrder(node.right, result);
            result.push(node.value);
        }
        return result;
    }

    /**
     * Level-order traversal (BFS)
     */
    levelOrder() {
        if (!this.root) return [];
        
        const result = [];
        const queue = [this.root];
        
        while (queue.length) {
            const node = queue.shift();
            result.push(node.value);
            
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        
        return result;
    }

    /**
     * Calculate height of tree
     * Time: O(n)
     */
    height(node = this.root) {
        if (!node) return -1;
        return 1 + Math.max(this.height(node.left), this.height(node.right));
    }

    /**
     * Check if tree is balanced
     */
    isBalanced(node = this.root) {
        if (!node) return true;
        
        const leftHeight = this.height(node.left);
        const rightHeight = this.height(node.right);
        
        return Math.abs(leftHeight - rightHeight) <= 1 &&
               this.isBalanced(node.left) &&
               this.isBalanced(node.right);
    }

    /**
     * Count total nodes
     */
    size(node = this.root) {
        if (!node) return 0;
        return 1 + this.size(node.left) + this.size(node.right);
    }

    /**
     * Find path to a value
     */
    findPath(value, node = this.root, path = []) {
        if (!node) return null;
        
        path.push(node.value);
        
        if (node.value === value) return path;
        
        if (value < node.value) {
            return this.findPath(value, node.left, path);
        } else {
            return this.findPath(value, node.right, path);
        }
    }

    /**
     * Validate if tree is a valid BST
     */
    isValidBST(node = this.root, min = -Infinity, max = Infinity) {
        if (!node) return true;
        
        if (node.value <= min || node.value >= max) return false;
        
        return this.isValidBST(node.left, min, node.value) &&
               this.isValidBST(node.right, node.value, max);
    }
}

// Demonstration
console.log('='.repeat(70));
console.log('BINARY SEARCH TREE DEMONSTRATION');
console.log('='.repeat(70));

const bst = new BinarySearchTree();

// Insert values
console.log('\n1. INSERTION');
[50, 30, 70, 20, 40, 60, 80].forEach(val => bst.insert(val));
console.log('Inserted: 50, 30, 70, 20, 40, 60, 80');

// Traversals
console.log('\n2. TRAVERSALS');
console.log('In-order:', bst.inOrder());
console.log('Pre-order:', bst.preOrder());
console.log('Post-order:', bst.postOrder());
console.log('Level-order:', bst.levelOrder());

// Search
console.log('\n3. SEARCH');
console.log('Search 40:', bst.search(40));
console.log('Search 100:', bst.search(100));

// Properties
console.log('\n4. TREE PROPERTIES');
console.log('Height:', bst.height());
console.log('Size:', bst.size());
console.log('Min:', bst.findMin());
console.log('Max:', bst.findMax());
console.log('Is Balanced:', bst.isBalanced());
console.log('Is Valid BST:', bst.isValidBST());

// Path finding
console.log('\n5. PATH FINDING');
console.log('Path to 40:', bst.findPath(40));

// Deletion
console.log('\n6. DELETION');
bst.delete(30);
console.log('After deleting 30:', bst.inOrder());

console.log('\n' + '='.repeat(70));

module.exports = { TreeNode, BinarySearchTree };
