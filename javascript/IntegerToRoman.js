/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
  var str = [
    ['I', 'V'],
    ['X', 'L'],
    ['C', 'D'],
    ['M']
  ];
  var res = '';
  var i = 0;
  var tmp = 0;
  while (num > 0) {
    tmp = num % 10;
    if (tmp === 9) {
      res = str[i][0] + str[i + 1][0] + res;
    } else if (tmp >= 5) {
      res = str[i][1] + str[i][0].repeat(tmp - 5) + res;
    } else if (tmp === 4) {
      res = str[i][0] + str[i][1] + res;
    } else {
      res = str[i][0].repeat(tmp) + res;
    }
    num = Math.floor(num / 10);
    i++;
  }
  return res;
};
