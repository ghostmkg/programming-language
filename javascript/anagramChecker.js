function isAnagram(str1, str2) {
    // Remove spaces and convert to lowercase
    const normalize = str => str.replace(/\s+/g, '').toLowerCase();

    str1 = normalize(str1);
    str2 = normalize(str2);

    if (str1.length !== str2.length) return false;

    // Sort and compare
    return str1.split('').sort().join('') === str2.split('').sort().join('');
}

// Example usage
const s1 = "Listen";
const s2 = "Silent";

if (isAnagram(s1, s2)) {
    console.log(`${s1} and ${s2} are anagrams.`);
} else {
    console.log(`${s1} and ${s2} are NOT anagrams.`);
} 