/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let  newArr=[]
   for(let i=0;i<arr.length;i++)
   {
    //fn jis tarah ka modification ya transformation bolega vesa hi karna 
    // padega 
    newArr[i]=fn(arr[i],i);
   }
   return newArr;
};