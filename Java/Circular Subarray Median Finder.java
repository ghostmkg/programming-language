import java.util.*;

public class CircularMedian {
    public static List<Double> medianSlidingWindow(int[] nums, int k) {
        List<Double> res = new ArrayList<>();
        TreeMap<Integer, Integer> window = new TreeMap<>();
        for (int i = 0; i < nums.length + k - 1; i++) {
            int num = nums[i % nums.length];
            window.put(num, window.getOrDefault(num, 0) + 1);
            if (i >= k) {
                int out = nums[(i - k) % nums.length];
                window.put(out, window.get(out) - 1);
                if (window.get(out) == 0) window.remove(out);
            }
            if (i >= k - 1)
                res.add(findMedian(window, k));
        }
        return res;
    }

    private static double findMedian(TreeMap<Integer, Integer> map, int k) {
        int count = 0;
        for (int key : map.keySet()) {
            count += map.get(key);
            if (count >= (k + 1) / 2)
                return k % 2 == 1 ? key : (key + map.higherKey(key)) / 2.0;
        }
        return 0;
    }

    public static void main(String[] args) {
        int[] arr = {2, 1, 5, 7, 2, 0, 5};
        System.out.println(medianSlidingWindow(arr, 3));
    }
}
