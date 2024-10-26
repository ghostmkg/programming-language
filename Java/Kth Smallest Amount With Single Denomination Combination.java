import java.math.BigInteger;

class Solution {
    public long findKthSmallest(int[] coins, int k) {
        long left = k, right = 50000000000L;
        while (left < right) {
            long mid = (left + right) / 2;
            if (findKthSmallest(coins, mid, 1, 0, 0) < k) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }

    private long findKthSmallest(int[] coins, long k, long v, int index, int flag) {
        return index < coins.length ? findKthSmallest(coins, k, v, index + 1, flag) + findKthSmallest(coins, k, v * coins[index] / BigInteger.valueOf(v).gcd(BigInteger.valueOf(coins[index])).longValue(), index + 1, flag + 1) : flag > 0 ? flag % 2 > 0 ? k / v : -k / v : 0;
    }
}    