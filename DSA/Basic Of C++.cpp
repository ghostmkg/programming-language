#include <iostream>
using namespace std;

int main() {
  int x = 10;
  int y = 20;
  int marks;
  cout << "Enter your marks: ";
  cin >> marks;

  // If condition
  if (x < y) {
    cout << "x is less than y" << endl;
  }

  // If-else condition
  if (x > y) {
    cout << "x is greater than y" << endl;
  } else {
    cout << "x is not greater than y" << endl;
  }

  // If-else if condition
  if (x > y) {
    cout << "x is greater than y" << endl;
  } else if (x == y) {
    cout << "x is equal to y" << endl;
  } else {
    cout << "x is less than y" << endl;
  }

  // If-else if-else condition
  if (x > y) {
    cout << "x is greater than y" << endl;
  } else if (x == y) {
    cout << "x is equal to y" << endl;
  } else if (x < y) {
    cout << "x is less than y" << endl;
  } else {
    cout << "Unexpected condition" << endl;
  }
  if (marks >= 90) {
    cout << "A grade";
  } else if (marks >= 80) {
    cout << "B grade";
  } else if (marks >= 60) {
    cout << "C grade";
  } else if (marks >= 40) {
    cout << "D grade";
  } else {
    cout << "F grade";
  }

  // Nested if-else condition
  if (x == 10) {
    if (y == 20) {
      cout << "x is 10 and y is 20" << endl;
    } else {
      cout << "x is 10 but y is not 20" << endl;
    }
  } else {
    cout << "x is not 10" << endl;
  }

  if (marks >= 90) {
    cout << "A grade";
  } else {
    if (marks >= 80) {
      cout << "B grade";
    } else {
      if (marks >= 60) {
        cout << "C grade";
      } else {
        if (marks >= 40) {
          cout << "D grade";
        } else {
          cout << "F grade";
        }
      }
    }
  }

  // Loop - For

  // for (int i = 5; (i >= 5 && i <= 10); i++) {
  //   cout << i << endl;
  // }

  // for (int i = 0; i <= 5; i++) {
  //   cout << i << endl;
  // }
  // In For Loop All Initialization,Condition, Updation Are not mandatory

  int i = 0;
  for (;;) {
    if (i < 5) {
      cout << i << endl;
      i = i + 1;
    }
  }

  return 0;
}
