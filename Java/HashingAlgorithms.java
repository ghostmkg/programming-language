/**
 * Hash Table and Hashing Algorithms in Java
 * ==========================================
 * 
 * Custom hash table implementation, collision resolution,
 * and common hashing problems.
 * 
 * @author Hacktoberfest 2025 Contributor
 */

package algorithms.hashing;

import java.util.*;

public class HashingAlgorithms {
    
    /**
     * Custom Hash Table with Separate Chaining
     */
    static class HashTable<K, V> {
        private static class Entry<K, V> {
            K key;
            V value;
            Entry<K, V> next;
            
            Entry(K key, V value) {
                this.key = key;
                this.value = value;
            }
        }
        
        private Entry<K, V>[] table;
        private int capacity;
        private int size;
        private static final double LOAD_FACTOR = 0.75;
        
        @SuppressWarnings("unchecked")
        public HashTable(int capacity) {
            this.capacity = capacity;
            this.table = new Entry[capacity];
            this.size = 0;
        }
        
        public HashTable() {
            this(16);
        }
        
        /**
         * Hash function - Time: O(1)
         */
        private int hash(K key) {
            return Math.abs(key.hashCode()) % capacity;
        }
        
        /**
         * Put key-value pair - Time: O(1) average
         */
        public void put(K key, V value) {
            if ((double) size / capacity >= LOAD_FACTOR) {
                resize();
            }
            
            int index = hash(key);
            Entry<K, V> entry = table[index];
            
            // Update if key exists
            while (entry != null) {
                if (entry.key.equals(key)) {
                    entry.value = value;
                    return;
                }
                entry = entry.next;
            }
            
            // Insert new entry at beginning
            Entry<K, V> newEntry = new Entry<>(key, value);
            newEntry.next = table[index];
            table[index] = newEntry;
            size++;
        }
        
        /**
         * Get value by key - Time: O(1) average
         */
        public V get(K key) {
            int index = hash(key);
            Entry<K, V> entry = table[index];
            
            while (entry != null) {
                if (entry.key.equals(key)) {
                    return entry.value;
                }
                entry = entry.next;
            }
            
            return null;
        }
        
        /**
         * Remove key - Time: O(1) average
         */
        public V remove(K key) {
            int index = hash(key);
            Entry<K, V> entry = table[index];
            Entry<K, V> prev = null;
            
            while (entry != null) {
                if (entry.key.equals(key)) {
                    if (prev == null) {
                        table[index] = entry.next;
                    } else {
                        prev.next = entry.next;
                    }
                    size--;
                    return entry.value;
                }
                prev = entry;
                entry = entry.next;
            }
            
            return null;
        }
        
        /**
         * Resize and rehash - Time: O(n)
         */
        @SuppressWarnings("unchecked")
        private void resize() {
            int newCapacity = capacity * 2;
            Entry<K, V>[] oldTable = table;
            
            table = new Entry[newCapacity];
            capacity = newCapacity;
            size = 0;
            
            for (Entry<K, V> entry : oldTable) {
                while (entry != null) {
                    put(entry.key, entry.value);
                    entry = entry.next;
                }
            }
        }
        
        public int size() {
            return size;
        }
        
        public boolean containsKey(K key) {
            return get(key) != null;
        }
    }
    
    /**
     * Find first non-repeating character
     * Time: O(n), Space: O(1) - limited to 256 characters
     */
    public static char firstNonRepeating(String s) {
        Map<Character, Integer> freq = new LinkedHashMap<>();
        
        for (char c : s.toCharArray()) {
            freq.put(c, freq.getOrDefault(c, 0) + 1);
        }
        
        for (Map.Entry<Character, Integer> entry : freq.entrySet()) {
            if (entry.getValue() == 1) {
                return entry.getKey();
            }
        }
        
        return '\0';
    }
    
    /**
     * Two Sum Problem
     * Time: O(n), Space: O(n)
     */
    public static int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];
            
            if (map.containsKey(complement)) {
                return new int[] {map.get(complement), i};
            }
            
            map.put(nums[i], i);
        }
        
        return new int[] {-1, -1};
    }
    
    /**
     * Check if arrays are equal (ignoring order)
     * Time: O(n), Space: O(n)
     */
    public static boolean areArraysEqual(int[] arr1, int[] arr2) {
        if (arr1.length != arr2.length) return false;
        
        Map<Integer, Integer> freq = new HashMap<>();
        
        for (int num : arr1) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        for (int num : arr2) {
            if (!freq.containsKey(num)) return false;
            
            int count = freq.get(num);
            if (count == 1) {
                freq.remove(num);
            } else {
                freq.put(num, count - 1);
            }
        }
        
        return freq.isEmpty();
    }
    
    /**
     * Longest consecutive sequence
     * Time: O(n), Space: O(n)
     */
    public static int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        
        int maxLength = 0;
        
        for (int num : set) {
            // Only start counting if num is start of sequence
            if (!set.contains(num - 1)) {
                int currentNum = num;
                int currentLength = 1;
                
                while (set.contains(currentNum + 1)) {
                    currentNum++;
                    currentLength++;
                }
                
                maxLength = Math.max(maxLength, currentLength);
            }
        }
        
        return maxLength;
    }
    
    /**
     * Subarray sum equals K
     * Time: O(n), Space: O(n)
     */
    public static int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixSum = new HashMap<>();
        prefixSum.put(0, 1);
        
        int sum = 0;
        int count = 0;
        
        for (int num : nums) {
            sum += num;
            
            if (prefixSum.containsKey(sum - k)) {
                count += prefixSum.get(sum - k);
            }
            
            prefixSum.put(sum, prefixSum.getOrDefault(sum, 0) + 1);
        }
        
        return count;
    }
    
    /**
     * Find duplicates in array
     * Time: O(n), Space: O(n)
     */
    public static List<Integer> findDuplicates(int[] nums) {
        Map<Integer, Integer> freq = new HashMap<>();
        List<Integer> duplicates = new ArrayList<>();
        
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        for (Map.Entry<Integer, Integer> entry : freq.entrySet()) {
            if (entry.getValue() > 1) {
                duplicates.add(entry.getKey());
            }
        }
        
        return duplicates;
    }
    
    /**
     * Group anagrams
     * Time: O(n * k log k) where k is max string length
     * Space: O(n * k)
     */
    public static List<List<String>> groupAnagrams(String[] words) {
        Map<String, List<String>> map = new HashMap<>();
        
        for (String word : words) {
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(word);
        }
        
        return new ArrayList<>(map.values());
    }
    
    /**
     * Top K frequent elements
     * Time: O(n log k), Space: O(n)
     */
    public static List<Integer> topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        
        for (int num : nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        
        PriorityQueue<Map.Entry<Integer, Integer>> pq = 
            new PriorityQueue<>((a, b) -> b.getValue() - a.getValue());
        
        pq.addAll(freq.entrySet());
        
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < k && !pq.isEmpty(); i++) {
            result.add(pq.poll().getKey());
        }
        
        return result;
    }
    
    /**
     * Demonstration
     */
    public static void demonstrate() {
        System.out.println("=".repeat(70));
        System.out.println("HASHING ALGORITHMS DEMONSTRATION");
        System.out.println("=".repeat(70));
        
        // Custom Hash Table
        System.out.println("\n1. CUSTOM HASH TABLE");
        HashTable<String, Integer> ht = new HashTable<>();
        ht.put("one", 1);
        ht.put("two", 2);
        ht.put("three", 3);
        System.out.println("   Get 'two': " + ht.get("two"));
        System.out.println("   Size: " + ht.size());
        
        // First Non-Repeating Character
        System.out.println("\n2. FIRST NON-REPEATING CHARACTER");
        String s = "leetcode";
        System.out.println("   String: " + s);
        System.out.println("   First non-repeating: " + firstNonRepeating(s));
        
        // Two Sum
        System.out.println("\n3. TWO SUM");
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println("   Array: " + Arrays.toString(nums));
        System.out.println("   Target: " + target);
        System.out.println("   Indices: " + Arrays.toString(result));
        
        // Longest Consecutive Sequence
        System.out.println("\n4. LONGEST CONSECUTIVE SEQUENCE");
        int[] arr = {100, 4, 200, 1, 3, 2};
        System.out.println("   Array: " + Arrays.toString(arr));
        System.out.println("   Longest: " + longestConsecutive(arr));
        
        // Subarray Sum
        System.out.println("\n5. SUBARRAY SUM EQUALS K");
        int[] arr2 = {1, 1, 1};
        int k = 2;
        System.out.println("   Array: " + Arrays.toString(arr2));
        System.out.println("   K: " + k);
        System.out.println("   Count: " + subarraySum(arr2, k));
        
        // Group Anagrams
        System.out.println("\n6. GROUP ANAGRAMS");
        String[] words = {"eat", "tea", "tan", "ate", "nat", "bat"};
        System.out.println("   Words: " + Arrays.toString(words));
        System.out.println("   Groups: " + groupAnagrams(words));
        
        // Top K Frequent
        System.out.println("\n7. TOP K FREQUENT ELEMENTS");
        int[] arr3 = {1, 1, 1, 2, 2, 3};
        System.out.println("   Array: " + Arrays.toString(arr3));
        System.out.println("   Top 2: " + topKFrequent(arr3, 2));
        
        System.out.println("\n" + "=".repeat(70));
    }
    
    public static void main(String[] args) {
        demonstrate();
    }
}
