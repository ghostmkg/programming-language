// priorityQueue.js
// Binary-heap Priority Queue with custom comparator (default: min-heap).
// API: push, pop, peek, size, isEmpty, clear.

export class PriorityQueue {
  /**
   * @param {(a:any,b:any)=>number} [compare] - return <0 if a<b, 0 if equal, >0 if a>b
   */
  constructor(compare = (a, b) => (a < b ? -1 : a > b ? 1 : 0)) {
    this._heap = [];
    this._cmp = compare;
  }

  get size() { return this._heap.length; }
  isEmpty() { return this.size === 0; }
  clear() { this._heap.length = 0; }

  peek() { return this._heap[0]; }

  push(value) {
    this._heap.push(value);
    this.#siftUp(this.size - 1);
  }

  pop() {
    const n = this.size;
    if (n === 0) return undefined;
    this.#swap(0, n - 1);
    const out = this._heap.pop();
    this.#siftDown(0);
    return out;
  }

  #parent(i) { return ((i - 1) >> 1); }
  #left(i) { return (i << 1) + 1; }
  #right(i) { return (i << 1) + 2; }

  #swap(i, j) {
    const a = this._heap;
    [a[i], a[j]] = [a[j], a[i]];
  }

  #siftUp(i) {
    for (let p = this.#parent(i); i > 0 && this._cmp(this._heap[i], this._heap[p]) < 0; p = this.#parent(i)) {
      this.#swap(i, p);
      i = p;
    }
  }

  #siftDown(i) {
    for (;;) {
      const l = this.#left(i), r = this.#right(i);
      let best = i;
      if (l < this.size && this._cmp(this._heap[l], this._heap[best]) < 0) best = l;
      if (r < this.size && this._cmp(this._heap[r], this._heap[best]) < 0) best = r;
      if (best === i) break;
      this.#swap(i, best);
      i = best;
    }
  }
}

// // Example:
// const pq = new PriorityQueue();            // min-heap numbers
// [5,1,4,2,3].forEach(x => pq.push(x));
// while (!pq.isEmpty()) console.log(pq.pop());  // 1,2,3,4,5
