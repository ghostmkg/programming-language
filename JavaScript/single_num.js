// 👉🏻 Q. finding the unique/single element from an array.
function singleNumber(nums){
  let result=0;
  for(let num of nums){
      result ^= num; // XOR all numbers
  }
  return result;  // The single number
}

console.log(singleNumber([4, 1, 2, 1, 2])); // Output: 4
console.log(singleNumber([2, 2, 1])); // Output: 1


//👉🏻logic of the Code:
// 1.The variable result starts at 0.
// 2.The loop iterates through each number in the nums array, applying the XOR operation with result.
// 3.Since every number that appears twice cancels itself out (because of the properties of XOR), the only number that remains is the one that appears once.

//👉🏻time complexity=O(n)  --loop iterate each and every value of array.
//👉🏻space complexity=O(1)
