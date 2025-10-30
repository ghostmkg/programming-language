// lru-cache.js
// Tiny LRU cache with O(1) get/put using Map (insertion order).
// API: get/put/has/delete/clear/size. Returns -1 on miss to match your original.

export class LRUCache {
  /**
   * @param {number} capacity - max number of entries (>=1)
   */
  constructor(capacity) {
    if (!Number.isInteger(capacity) || capacity < 1) {
      throw new Error("capacity must be an integer >= 1");
    }
    this.capacity = capacity;
    this.cache = new Map(); // key -> value (MRU at the end)
  }

  /**
   * @param {any} key
   * @returns {any} value or -1 if not found
   */
  get(key) {
    if (!this.cache.has(key)) return -1;
    const value = this.cache.get(key);
    // move to MRU
    this.cache.delete(key);
    this.cache.set(key, value);
    return value;
  }

  /**
   * @param {any} key
   * @param {any} value
   */
  put(key, value) {
    if (this.cache.has(key)) this.cache.delete(key);
    this.cache.set(key, value);
    if (this.cache.size > this.capacity) {
      // evict LRU (first key)
      const lruKey = this.cache.keys().next().value;
      this.cache.delete(lruKey);
    }
  }

  /**
   * @param {any} key
   * @returns {boolean}
   */
  has(key) {
    return this.cache.has(key);
  }

  /**
   * @param {any} key
   * @returns {boolean}
   */
  delete(key) {
    return this.cache.delete(key);
  }

  clear() {
    this.cache.clear();
  }

  get size() {
    return this.cache.size;
  }
}
