public class SmallestString {
    static String minStr;

    static void findMin(char[] str, int k) {
        if (k == 0) return;
        int n = str.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (str[j] < str[i]) {
                    swap(str, i, j);
                    String curr = new String(str);
                    if (curr.compareTo(minStr) < 0)
                        minStr = curr;
                    findMin(str, k - 1);
                    swap(str, i, j);
                }
            }
        }
    }

    static void swap(char[] arr, int i, int j) {
        char t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    public static void main(String[] args) {
        String s = "cbad";
        int k = 2;
        minStr = s;
        findMin(s.toCharArray(), k);
        System.out.println("Smallest: " + minStr);
    }
}
