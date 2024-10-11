public class Leetcode_1813 {
    public boolean areSentencesSimilar(String sentence1, String sentence2) {
        String[] s1Words = sentence1.split(" ");
        String[] s2Words = sentence2.split(" ");
        int n1 = s1Words.length;
        int n2 = s2Words.length;
        int left = 0, r1 = n1 - 1, r2 = n2 - 1;

        while (s1Words[left].equals(s2Words[left])) {
            left++;
            if ((left == n1) || (left == n2)) return true;
        }
        
        while (s1Words[r1].equals(s2Words[r2])) {
            if ((r1 == left) || (r2 == left)) return true;
            r1--;
            r2--;
        }
        return false;
    }
    public static void main(String[] args) {
        Leetcode_1813 obj = new Leetcode_1813();
        System.out.println(obj.areSentencesSimilar("My name is Haley", "My Haley"));
    }
}
