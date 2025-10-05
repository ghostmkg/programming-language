// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
// determine if the input string is valid.

// An input string is valid if:
//     1- Open brackets must be closed by the same type of brackets.
//     2- Open brackets must be closed in the correct order.
//     3- Every close bracket has a corresponding open bracket of the same type.

// Example 1:
//     Input: s = "()"
//     Output: true

// Example 2:
//     Input: s = "()[]{}"
//     Output: true

// Example 3:
//     Input: s = "(]"
//     Output: false

// Example 4:
//     Input: s = "([])"
//     Output: true

// Example 5:
//     Input: s = "([)]"
//     Output: false

//  Constraints:
//     --1 <= s.length <= 104
//     --s consists of parentheses only '()[]{}'.

//Solution Function in Js.
var isValid = function (s) {
  let stack = [];
  for (let i = 0; i < s.length; i++) {
    if (s[i] == "(" || s[i] == "[" || s[i] == "{") {
      stack.push(s[i]);
    } else {
      if (stack.length == 0) {
        return false;
      }
      let top = stack.pop();
      if (top == "(" && s[i] != ")") {
        return false;
      }
      if (top == "[" && s[i] != "]") {
        return false;
      }
      if (top == "{" && s[i] != "}") {
        return false;
      }
    }
  }
  if (stack.length == 0) {
    return true;
  } else {
    return false;
  }
};
