let input;

function reset() {
  d3.selectAll('svg').remove();
}

function treeAndArray() {
  reset();
  let inputText = document.getElementById("array-input")
  document.querySelector('#visual-title').innerHTML = "Binary Tree And Array";
  document.querySelector('#instructions').innerHTML = "Click a value in the binary tree or array to highlight its corresponding location in the data structure.";
  if (inputText.value !== '') {
      input = inputText.value.trim().split(/\s+|\,+/g).map((num) => parseInt(num));
      createBinaryTreeAndArr(input)
  }
}

function heapify() {
  reset();
  let inputText = document.getElementById("array-input")
  if (inputText.value !== '') {
    input = inputText.value.trim().split(/\s+|\,+/g).map((num) => parseInt(num));
    makeHeap(input, input.length);
    createBinaryTreeAndArr(input);
    document.getElementById('instructions').innerHTML = "<p> Parent's value is always greater than or equal to the values of its children.</p>";
    document.getElementById('visual-title').innerHTML = "Max-Heap Binary Tree And Array";
  }
}

function createBinaryTreeAndArr(arr) {
  arrayContainer = createContainer("array-visual", arr, arr.length * 60, 100);
  let tree = new Tree()
  tree.createBinaryTree(input)
  createArray(arr, 2, 30, 50, 50);
}

function createBinarySearchTree() {
  let inputText = document.getElementById("array-input")
  if (inputText.value !== '') {
    reset();
    input = inputText.value.trim().split(/\s+|\,+/g).map((num) => parseInt(num));
    input.sort((a, b) => a - b);
    document.querySelector('#visual-title').innerHTML = "Binary Search Tree";
    document.querySelector('#instructions').innerHTML = "The input data sorted and arranged into a Binary Search Tree.";
    let tree = new Tree();
    tree.createBinarySearchTree(input)
  }
}

//default values
input = [10, 20, 60, 30, 70, 40, 50];
let inputTest = document.getElementById("array-input")
inputTest.value = input;
createBinaryTreeAndArr(input);
