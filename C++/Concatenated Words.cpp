#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <string>

using namespace std;

class Solution {
public:
    int n;  // Number of words
    unordered_map<string, bool> mp;  // Memoization map for already processed words

    // Helper function to check if the word can be formed by concatenating two or more words from the set
    bool isConcat(string word, unordered_set<string>& st) {
        // If the word has already been processed, return the stored result
        if(mp.find(word) != mp.end())
            return mp[word];
        
        int l = word.length();
        
        // Try breaking the word into two parts: prefix and suffix
        for(int i = 0; i < l; i++) {
            string prefix = word.substr(0, i + 1);
            string suffix = word.substr(i + 1);
            
            // If the prefix is in the set and the suffix can either be a concatenated word or a direct word in the set
            if((st.find(prefix) != st.end() && isConcat(suffix, st)) ||
               (st.find(prefix) != st.end() && st.find(suffix) != st.end()))
                return mp[word] = true;  // Mark the word as concatenated and store the result
        }

        return mp[word] = false;  // If not concatenated, return false and store the result
    }

    // Main function to find all concatenated words in the dictionary
    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        n = words.size();
        mp.clear();  // Clear the memoization map
        vector<string> result;
        unordered_set<string> st(begin(words), end(words));  // Insert all words into a set for fast lookup
        
        // For each word, check if it can be formed by concatenating other words
        for(int i = 0; i < n; i++) {
            if(isConcat(words[i], st))
                result.push_back(words[i]);
        }
        
        return result;  // Return the result containing all concatenated words
    }
};

int main() {
    // Example usage
    vector<string> words = {"cat", "cats", "catsdogcats", "dog", "dogcatsdog", "rat", "ratcatdogcat"};
    
    Solution solution;
    vector<string> concatenatedWords = solution.findAllConcatenatedWordsInADict(words);
    
    cout << "Concatenated Words in the Dictionary:" << endl;
    for(string word : concatenatedWords) {
        cout << word << endl;
    }
    
    return 0;
}
