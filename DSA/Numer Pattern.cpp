#include <stdio.h>

int main() {

  // Pattern 1
  //  12345
  //  1234
  //  123
  //  12
  //  1

  // for (int i = 5; i >= 1; i--) {
  //     for (int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // // Generic
  // for (int i = rows; i >= 1; i--) {
  //   for (int j = 1; j <= i; j++) {
  //     cout << j;
  //   }
  //   cout << endl;
  // }

  // Pattern 2
  // 12345
  // 2345
  // 345
  // 45
  // 5

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = i; j <= 5; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 3
  // 54321
  // 4321
  // 321
  // 21
  // 1

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = i; j >= 1; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 4
  // 54321
  // 5432
  // 543
  // 54
  // for(int i = 5; i >= 1; i--) {
  //     for(int j = 5; j >= i; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 5
  // 1
  // 12
  // 123
  // 1234
  // 12345

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 6
  // 5
  // 45
  // 345
  // 2345
  // 12345

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = i; j <= 5; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 7
  // 1
  // 21
  // 321
  // 4321
  // 54321

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = i; j >= 1; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 8
  // 5
  // 54
  // 543
  // 5432
  // 54321

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = 5; j >= i; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 9
  // 1
  // 22
  // 333
  // 4444
  // 55555

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << i;
  //     }
  //     cout << endl;
  // }

  // Pattern 10
  // 5
  // 44
  // 333
  // 2222
  // 11111

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = i; j >= 1; j--) {
  //         cout << i;
  //     }
  //     cout << endl;
  // }

  // Pattern 11
  // 55555
  // 4444
  // 333
  // 22
  // 1

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << i;
  //     }
  //     cout << endl;
  // }

  // Pattern 12
  // 11111
  // 2222
  // 333
  // 44
  // 5

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= 6 - i; j++) {
  //         cout << i;
  //     }
  //     cout << endl;
  // }

  // Pattern 13
  // 12345
  // 4321
  // 123
  // 21
  // 1

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 14
  // 1234567
  // 12345
  // 123
  // 1

  // for(int i = 7; i >= 1; i -= 2) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 15
  // 1
  // 01
  // 101
  // 0101

  // for(int i = 0; i < 4; i++) {
  //     for(int j = i; j >= 0; j--) {
  //         if(j % 2 == 0) cout << "1";
  //         else cout << "0";
  //     }
  //     cout << endl;
  // }

  // Pattern 16
  // 13579
  // 3579
  // 579
  // 79
  // 9

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = i; j <= 9; j += 2) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 17
  // 1
  // 2 4
  // 1 3 5
  // 2 4 6 8
  // 1 3 5 7 9

  // for(int i = 1; i <= 5; i++) {
  //     if(i % 2 == 0) {
  //         for(int j = 2; j <= i + 1; j += 2) {
  //             cout << j << " ";
  //         }
  //     }
  //     else {
  //         for(int j = 1; j <= i; j += 2) {
  //             cout << j << " ";
  //         }
  //     }
  //     cout << endl;
  // }

  // Pattern 18
  // 55555
  // 45555
  // 34555
  // 23455
  // 12345

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = 5; j >= i; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 19
  // 1
  // 23
  // 456
  // 78910

  // int num = 1;
  // for(int i = 1; i <= 4; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << num++;
  //     }
  //     cout << endl;
  // }

  // Pattern 20
  // 1
  // 10
  // 101
  // 1010
  // 10101

  // int n = 1;
  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << n % 2;
  //         n++;
  //     }
  //     cout << endl;
  // }

  // Pattern 21
  // 1
  // 2 6
  // 3 7 10
  // 4 8 11 13
  // 5 9 12 14 15

  // for(int i = 1; i <= 5; i++) {
  //     int num = i;
  //     for(int j = 1; j <= i; j++) {
  //         cout << num << " ";
  //         num += 5 - j;
  //     }
  //     cout << endl;
  // }

  // Pattern 22
  // 1
  // 123
  // 12345
  // 1234567

  // int num = 1;
  // for(int i = 1; i <= 4; i++) {
  //     for(int j = 1; j <= 2 * i - 1; j++) {
  //         cout << num++;
  //     }
  //     cout << endl;
  // }

  // Pattern 23
  // 12344321
  // 123**321
  // 12****21
  // 1******1

  // for(int i = 1; i <= 4; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     for(int j = 1; j <= 8 - 2 * i; j++) {
  //         cout << "*";
  //     }
  //     for(int j = i; j >= 1; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 24
  //      1
  //    2 3 4
  //  5 6 7 8 9

  // int num = 1;
  // for(int i = 0; i < 3; i++) {
  //     for(int j = 0; j < 2 - i; j++) {
  //         cout << "  ";
  //     }
  //     for(int j = 0; j < i + 1; j++) {
  //         cout << num++;
  //         if(j != i) cout << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 25
  // 1   2   3   4   5   6   7   8   9   10
  // 36  37  38  39  40  41  42  43  44  11
  // 35  64  65  66  67  68  69  70  45  12
  // 34  63  84  85  86  87  88  71  46  13
  // 33  62  83  96  97  98  89  72  47  14
  // 32  61  82  95  100 99  90  73  48  15
  // 31  60  81  94  93  92  91  74  49  16
  // 30  59  80  79  78  77  76  75  50  17
  // 29  58  57  56  55  54  53  52  51  18
  // 28  27  26  25  24  23  22  21  20  19

  // int n = 1;
  // for(int i = 1; i <= 10; i++) {
  //     for(int j = 1; j <= 10; j++) {
  //         cout << setw(3) << n++;
  //     }
  //     cout << endl;
  //     if(i < 9) {
  //         n = n + i;
  //     }
  //     else {
  //         n = n - 17;
  //     }
  // }

  // Pattern 26
  // 11111
  // 2222
  // 333
  // 22
  // 1

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << i;
  //     }
  //     cout << endl;
  // }

  // Pattern 27
  // 5432*
  // 543*1
  // 54*21
  // 5*321
  // *4321

  // for(int i = 5; i >= 1; i--) {
  //     for(int j = 5; j >= 1; j--) {
  //         if(j == i)
  //             cout << "*";
  //         else
  //             cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 28
  // 1
  // 121
  // 12321
  // 1234321

  // for(int i = 1; i <= 4; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         if (j == 1 || j == i)
  //             cout << j;
  //         else
  //             cout << " ";
  //     }
  //     for(int j = i - 1; j >= 1; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 29
  // 0
  // 909
  // 89098
  // 7890987
  // 678909876
  // 56789098765
  // 4567890987654
  // 345678909876543
  // 23456789098765432
  // 1234567890987654321

  // for(int i = 0; i <= 9; i++) {
  //     for(int j = i; j >= 0; j--) {
  //         cout << j;
  //     }
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 30
  // 1        1
  // 12      21
  // 123    321
  // 1234  4321
  // 1234554321

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     for(int j = 1; j <= 10 - 2 * i; j++) {
  //         cout << " ";
  //     }
  //     for(int j = i; j >= 1; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 31
  //     1
  //    21
  //   321
  //  4321
  // 54321

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= 5 - i; j++) {
  //         cout << " ";
  //     }
  //     for(int j = i; j >= 1; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 32
  // 1
  // 232
  // 45654
  // 78910987

  // int num = 1;
  // for(int i = 1; i <= 4; i++) {
  //     for(int j = 1; j <= 2 * i - 1; j++) {
  //         cout << num++;
  //     }
  //     for(int j = 1; j <= i - 1; j++) {
  //         cout << num - 2 * i;
  //     }
  //     cout << endl;
  // }

  // Pattern 33
  // 1
  // 2*2
  // 3*3*3
  // 4*4*4*4
  // 4*4*4*4
  // 3*3*3
  // 2*2
  // 1

  // int n = 4;
  // for (int i = 1; i >= -3; i -= 2) {
  //     for (int j = 1; j <= abs(i); j++) {
  //         cout << n;
  //         if (j < abs(i)) cout << "*";
  //     }
  //     cout << endl;
  // }

  // Pattern 34
  // 11
  // 12 13
  // 13 14 15
  // 14 15 16 17

  // for(int i = 1; i <= 4; i++) {
  //     int num = i;
  //     for(int j = 1; j <= i; j++) {
  //         cout << num++ << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 35
  //             1
  //           2 3
  //         4 5 6
  //      7 8 9 10
  // 11 12 13 14 15

  // int num = 1;
  // for(int i = 1; i <= 5; i++) {
  //     for(int k = 1; k <= 5 - i; k++) {
  //         cout << "   ";
  //     }
  //     for(int j = 1; j <= i; j++) {
  //         cout << setw(2) << num++ << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 36
  //     5
  //    54
  //   543
  //  5432
  // 54321

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= 5 - i; j++) {
  //         cout << " ";
  //     }
  //     for(int j = 5; j >= 6 - i; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 37
  // 1
  // 212
  // 32123
  // 4321234

  // for(int i = 1; i <= 4; i++) {
  //     for(int j = i; j >= 1; j--) {
  //         cout << j;
  //     }
  //     for(int j = 2; j <= i + 1; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 39
  // 1
  // 23
  // 345
  // 4567
  // 56789

  // int num = 1;
  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= i; j++) {
  //         cout << setw(2) << num++;
  //     }
  //     cout << endl;
  // }

  // Pattern 40
  //   1  2  3  4  5
  //   6  7  8  9
  //   10 11 12
  //   13 14
  //   15

  // int num = 1;
  // for(int i = 1; i <= 5; i++) {
  //     for(int k = 1; k < i; k++) {
  //         cout << "  ";
  //     }
  //     for(int j = 1; j <= 6 - i; j++) {
  //         cout << setw(2) << num++ << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 41
  // 1234
  // 2341
  // 3421
  // 4321

  // for(int i = 1; i <= 4; i++) {
  //     for(int j = i; j <= 4; j++) {
  //         cout << j;
  //     }
  //     for(int j = 1; j < i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 42
  // 11111
  // 0000
  // 111
  // 00
  // 1

  // for(int i = 5; i >= 1; i -= 2) {
  //     for(int j = 0; j < i; j++) {
  //         cout << "1";
  //     }
  //     cout << endl;
  //     for(int j = 0; j < i; j++) {
  //         cout << "0";
  //     }
  //     cout << endl;
  // }

  // Pattern 43
  //                  1
  //              4   9  16
  //         25  36  49  64  81
  //    100 121 144 169 196 225 256
  // 289 324 361 400 441 484 529 576 625

  // int num = 1;
  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= 5 - i; j++) {
  //         cout << "    ";
  //     }
  //     for(int j = 1; j <= i; j++) {
  //         cout << setw(4) << num * num++ << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 44
  // 11111
  // 1   1
  // 1   1
  // 1   1
  // 11111

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= 5; j++) {
  //         if(i == 1 || i == 5 || j == 1 || j == 5)
  //             cout << "1";
  //         else
  //             cout << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 45
  //     1
  //    1 2
  //   1 2 3
  //  1 2 3 4
  // 1 2 3 4 5

  // for(int i = 1; i <= 5; i++) {
  //     for(int j = 1; j <= 5 - i; j++) {
  //         cout << " ";
  //     }
  //     for(int j = 1; j <= i; j++) {
  //         cout << j << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 46
  //     1
  //    123
  //   12345
  //  1234567
  // 123456789
  //  1234567
  //   12345
  //    123
  //     1

  // for(int i = 1; i <= 9; i += 2) {
  //     for(int j = 1; j <= 5 - i / 2; j++) {
  //         cout << " ";
  //     }
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }
  // for(int i = 7; i >= 1; i -= 2) {
  //     for(int j = 1; j <= 5 - i / 2; j++) {
  //         cout << " ";
  //     }
  //     for(int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 47
  // *000*000*
  // 0*00*00*0
  // 00*0*0*00
  // 000***000

  // int n = 3;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= n; j++) {
  //         if (i == j) cout << "*";
  //         else cout << "0";
  //     }
  //     for (int j = n; j >= 1; j--) {
  //         if (j == i) cout << "*";
  //         else cout << "0";
  //     }
  //     cout << endl;
  // }

  // Pattern 48
  // 5 5 5 5 5 5 5 5 5
  // 5 4 4 4 4 4 4 4 5
  // 5 4 3 3 3 3 3 4 5
  // 5 4 3 2 2 2 3 4 5
  // 5 4 3 2 1 2 3 4 5
  // 5 4 3 2 2 2 3 4 5
  // 5 4 3 3 3 3 3 4 5
  // 5 4 4 4 4 4 4 4 5
  // 5 5 5 5 5 5 5 5 5

  // int n = 5;
  // for (int i = 1; i <= 2 * n - 1; i++) {
  //     for (int j = 1; j <= 2 * n - 1; j++) {
  //         cout << max(abs(n - i), abs(n - j)) + 1 << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 49
  // 1
  // 1 1
  // 1 2 1
  // 1 3 3 1
  // 1 4 6 4 1

  // int n = 5;
  // for (int i = 0; i < n; i++) {
  //     int coef = 1;
  //     for (int j = 0; j <= i; j++) {
  //         cout << coef << " ";
  //         coef = coef * (i - j) / (j + 1);
  //     }
  //     cout << endl;
  // }

  // Pattern 50
  // 1
  // 2 4
  // 3 6 9
  // 4 8 12 16
  // 5 10 15 20 25
  // 6 12 18 24 30 36
  // 7 14 21 28 35 42 49
  // 8 16 24 32 40 48 56 64
  // 9 18 27 36 45 54 63 72 81
  // 10 20 30 40 50 60 70 80 90 100

  // int rows = 10;
  // for(int i = 1; i <= rows; i++) {
  //     int num = i;
  //     for(int j = 1; j <= i; j++) {
  //         cout << num << " ";
  //         num += i - j;
  //     }
  //     cout << endl;
  // }

  // Pattern 51
  // 1
  // 1 2
  // 3 5 8
  // 13 21 34 55
  // 89 144 233 377 610

  // int rows = 5;
  // int a = 0, b = 1, c;
  // for (int i = 1; i <= rows; ++i) {
  //     for (int j = 1; j <= i; ++j) {
  //         cout << a << " ";
  //         c = a + b;
  //         a = b;
  //         b = c;
  //     }
  //     cout << endl;
  // }

  // Pattern 52
  // 11111
  // 10001
  // 10001
  // 10001
  // 11111

  // int rows = 5;
  // for(int i = 1; i <= rows; i++) {
  //     for(int j = 1; j <= rows; j++) {
  //         if(i == 1 || i == rows || j == 1 || j == rows)
  //             cout << "1";
  //         else
  //             cout << "0";
  //     }
  //     cout << endl;
  // }

  // Pattern 53
  // 1 2 3 4 5
  // 2 1 2 3 4
  // 3 2 1 2 3
  // 4 3 2 1 2
  // 5 4 3 2 1

  // int n = 5;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= n; j++) {
  //         cout << abs(i - j) + 1 << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 54
  // 1
  // 3 2
  // 4 5 6
  // 10 9 8 7
  // 11 12 13 14 15

  // int num = 1;
  // for (int i = 1; i <= 5; i++) {
  //     if (i % 2 == 1) {
  //         for (int j = 1; j <= i; j++) {
  //             cout << num++ << " ";
  //         }
  //     } else {
  //         int temp = num + i - 1;
  //         for (int j = 1; j <= i; j++) {
  //             cout << temp-- << " ";
  //         }
  //         num += i;
  //     }
  //     cout << endl;
  // }

  // Pattern 55
  // 1
  // 232
  // 34543
  // 4567654
  // 567898765

  // int n = 5;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= i; j++) {
  //         cout << j;
  //     }
  //     for (int j = i - 1; j >= 1; j--) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  // Pattern 56
  // 1     1
  //  2   2
  //   3 3
  //    4
  //   3 3
  //  2   2
  // 1     1

  // int n = 4;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= n - i; j++) {
  //         cout << " ";
  //     }
  //     cout << i;
  //     for (int j = 1; j < 2 * i - 1; j++) {
  //         cout << " ";
  //     }
  //     if (i != 1) {
  //         cout << i;
  //     }
  //     cout << endl;
  // }
  // for (int i = n - 1; i >= 1; i--) {
  //     for (int j = 1; j <= n - i; j++) {
  //         cout << " ";
  //     }
  //     cout << i;
  //     for (int j = 1; j < 2 * i - 1; j++) {
  //         cout << " ";
  //     }
  //     if (i != 1) {
  //         cout << i;
  //     }
  //     cout << endl;
  // }

  // Pattern 57
  // 1
  // 2 6
  // 3 7 10
  // 4 8 11 13
  // 5 9 12 14 15

  // int n = 5;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= i; j++) {
  //         if (j == 1)
  //             cout << i << " ";
  //         else if (i == n)
  //             cout << j + n - 1 << " ";
  //         else
  //             cout << j + i + n - 2 << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 58
  //         1
  //       1 2 1
  //     1 2 3 2 1
  //   1 2 3 4 3 2 1
  // 1 2 3 4 5 4 3 2 1

  // int n = 5;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= n - i; j++) {
  //         cout << "  ";
  //     }
  //     for (int j = 1; j <= i; j++) {
  //         cout << j << " ";
  //     }
  //     for (int j = i - 1; j >= 1; j--) {
  //         cout << j << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 59
  //       1
  //     2   2
  //   3       3
  // 4           4
  //   3       3
  //     2   2
  //       1

  // int n = 4;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= 2 * n - 1; j++) {
  //         if (j == n - i + 1 || j == n + i - 1)
  //             cout << i;
  //         else
  //             cout << " ";
  //     }
  //     cout << endl;
  // }
  // for (int i = n - 1; i >= 1; i--) {
  //     for (int j = 1; j <= 2 * n - 1; j++) {
  //         if (j == n - i + 1 || j == n + i - 1)
  //             cout << i;
  //         else
  //             cout << " ";
  //     }
  //     cout << endl;
  // }

  // Pattern 60
  // 1  2  3  4  5
  // 16          6
  // 15          7
  // 14          8
  // 13 12 11 10 9

  // int n = 5;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= n - i; j++) {
  //         cout << "   ";
  //     }
  //     for (int j = i; j >= 1; j--) {
  //         cout << setw(2) << j << " ";
  //     }
  //     for (int j = 1; j <= i - 2; j++) {
  //         cout << "    ";
  //     }
  //     if (i != 1)
  //         cout << setw(4) << i;
  //     cout << endl;
  // }

  // Pattern 61
  // 3 9 1 7 4
  // 9 1 7 4
  // 1 7 4
  // 7 4
  // 4

  // int N = 39714;
  // while (N > 0) {
  //     int temp = N;
  //     while (temp > 0) {
  //         cout << temp % 10 << " ";
  //         temp /= 10;
  //     }
  //     cout << endl;
  //     N /= 10;
  // }

  // Pattern 62
  // 1
  // 123
  // 12345
  // 1234567
  // 12345
  // 123
  // 1

  // int n = 4;
  // for (int i = 1; i <= n; i++) {
  //     for (int j = 1; j <= 2 * i - 1; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }
  // for (int i = n - 1; i >= 1; i--) {
  //     for (int j = 1; j <= 2 * i - 1; j++) {
  //         cout << j;
  //     }
  //     cout << endl;
  // }

  return 0;
}
