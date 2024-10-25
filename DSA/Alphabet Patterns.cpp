#include <iostream>
using namespace std;

int main() {

  // Pattern 1
  // A
  // AB
  // ABC
  // ABCD
  // ABCDE

  // char endChar = 'E';
  // for (char ch = 'A'; ch <= endChar; ch++) {
  //     for (char c = 'A'; c <= ch; c++) {
  //         cout << c;
  //     }
  //     cout << endl;
  // }

  // Pattern 2
  // E
  // DE
  // CDE
  // BCDE
  // ABCDE

  // char endChar = 'E';
  // for (char ch = endChar; ch >= 'A'; ch--) {
  //     for (char c = ch; c <= endChar; c++) {
  //         cout << c;
  //     }
  //     cout << endl;
  // }

  // Pattern 3
  // A
  // BA
  // CBA
  // DCBA
  // EDCBA

  // for (char ch = 'A'; ch <= 'E'; ch++) {
  //     for (char c = ch; c >= 'A'; c--) {
  //         cout << c;
  //     }
  //     cout << endl;
  // }

  // Pattern 4
  // E
  // ED
  // EDC
  // EDCB
  // EDCBA

  // for (char ch = 'E'; ch >= 'A'; ch--) {
  //     for (char c = 'E'; c >= ch; c--) {
  //         cout << c;
  //     }
  //     cout << endl;
  // }

  // Pattern 5
  // ABCDE
  // ABCD
  // ABC
  // AB
  // A

  // for (int i = 5; i >= 1; i--) {
  //     for (char j = 'A'; j <= 'A' + i - 1; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 6
  // ABCDE
  // BCDE
  // CDE
  // DE
  // E

  // for (char ch = 'A'; ch <= 'E'; ch++) {
  //     for (char c = ch; c <= 'E'; c++) {
  //         cout << c;
  //     }
  //     cout << endl;
  // }

  // Pattern 7
  // EDCBA
  // DCBA
  // CBA
  // BA
  // A

  // for (char ch = 'E'; ch >= 'A'; ch--) {
  //     for (char c = ch; c >= 'A'; c--) {
  //         cout << c;
  //     }
  //     cout << endl;
  // }

  // Pattern 8
  // EDCBA
  // EDCB
  // EDC
  // ED
  // E

  // for (char ch = 'E'; ch >= 'A'; ch--) {
  //     for (char c = 'E'; c >= ch; c--) {
  //         cout << c;
  //     }
  //     cout << endl;
  // }

  // Pattern 9
  // A
  // BB
  // CCC
  // DDDD
  // EEEEE

  // for (char ch = 'A'; ch <= 'E'; ch++) {
  //     for (int i = 1; i <= ch - 'A' + 1; i++) {
  //         cout << ch;
  //     }
  //     cout << endl;
  // }

  // Pattern 10
  // E
  // DD
  // CCC
  // BBBB
  // AAAAA

  // for (char ch = 'E'; ch >= 'A'; ch--) {
  //     for (int i = 'E' - ch + 1; i >= 1; i--) {
  //         cout << ch;
  //     }
  //     cout << endl;
  // }

  // Pattern 11
  // EEEEE
  // DDDD
  // CCC
  // BB
  // A

  // char ch = 'E';
  // while (ch >= 'A') {
  //     for (int i = 1; i <= ch - 'A' + 1; i++) {
  //         cout << ch;
  //     }
  //     cout << endl;
  //     ch--;
  // }

  // Pattern 12
  // AAAAA
  // BBBB
  // CCC
  // DD
  // E

  // char ch = 'A';
  // while (ch <= 'E') {
  //     for (int i = 'E' - ch + 1; i >= 1; i--) {
  //         cout << ch;
  //     }
  //     cout << endl;
  //     ch++;
  // }

  return 0;
}