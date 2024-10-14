public class Leetcode_567 {
    public boolean checkInclusion(String s1, String s2) {
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];
        int n1 = s1.length();
        int n2 = s2.length();
        int l = 0, r = n1;

        if (n2 < n1) return false;

        for (int i = 0; i < n1; i++) {
            freq1[s1.charAt(i) - 'a']++;
            freq2[s2.charAt(i) - 'a']++;
        }
        while (r <= n2) {
            if (isMatching(freq1, freq2)) return true;
            freq2[s2.charAt(l) - 'a']--;
            if (r < n2)
                freq2[s2.charAt(r) - 'a']++;
            l++;
            r++;
        }
        return false;
    }
    private boolean isMatching(int[] freq1, int[] freq2) {
        for (int i = 0; i < 26; i++) {
            if (freq1[i] != freq2[i]) return false;
        }
        return true;
    }
    public static void main(String[] args) {
        Leetcode_567 obj = new Leetcode_567();
        System.out.println(obj.checkInclusion("ab", "eidbaooo"));
    }
}
