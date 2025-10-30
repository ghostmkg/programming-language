class Solution {
public:
  vector<int> deleteElement(vector<int>& arr, int k) {
    vector<int> st; 
      for (int i = 0; i < arr.size(); i++) {
        while (!st.empty() && st.back() < arr[i] && k > 0) {
          st.pop_back();
          k--;
        }
      st.push_back(arr[i]);
      }
      while (k > 0 && !st.empty()) {
        st.pop_back();
        k--;
      }
    return st;
  }
};
