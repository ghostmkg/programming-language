//Find the Single Element
function singleNumber(nums) {
    let result = 0;
    for (let num of nums) {
        result ^= num; 
    }
    return result;
}

const nums = [4, 1, 2, 1, 2];
console.log(singleNumber(nums));

//Count the Number of 1 Bits
function hammingWeight(n) {
    let count = 0;
    while (n) {
        count += n & 1;
        n >>>= 1;
    }
    return count;
}

const n = 11;
console.log(hammingWeight(n));
