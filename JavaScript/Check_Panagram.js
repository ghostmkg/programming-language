let checkIfPangram = function(sentence) {
    
    let charSet=new Set();

    for(let char of sentence){
        charSet.add(char);
    }

    return charSet.size===26? true:false;
};

let sentence1 = "thequickbrownfoxjumpsoverthelazydog";
let sentence2 = "leetcode";

console.log(checkIfPangram(sentence1)); //true

console.log(checkIfPangram(sentence2)); //false
