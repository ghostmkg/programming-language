function reverseWords(s){
    let word=s.trim().split(/\s+/);
    let rev="";
    for(let i=word.length-1;i>0;i--){
        rev=rev+word[i]+" ";
    }
    return rev+word[0];
}

let s="the blue    is not sky   but bird ok";
console.log(reverseWords(s));