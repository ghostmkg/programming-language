// pLimit.js
// Minimal promise concurrency limiter (like p-limit). Queue tasks, run at most N at once.

/**
 * @typedef {() => Promise<any>} Task
 */

/**
 * Create a concurrency limiter.
 * @param {number} concurrency - number of tasks to run simultaneously (>=1)
 * @returns {{
 *  (fn: (...args:any[])=>Promise<any>|any, ...args:any[]): Promise<any>,
 *  activeCount: () => number,
 *  pendingCount: () => number,
 *  clearQueue: () => void
 * }}
 */
export function pLimit(concurrency = 4) {
  if (!Number.isInteger(concurrency) || concurrency < 1) {
    throw new Error("concurrency must be an integer >= 1");
  }

  /** @type {Task[]} */
  const queue = [];
  let active = 0;

  const next = () => {
    if (active >= concurrency) return;
    const task = queue.shift();
    if (!task) return;
    active++;
    task().finally(() => {
      active--;
      next();
    });
  };

  const run = (fn, ...args) => new Promise((resolve, reject) => {
    const task = async () => {
      try {
        resolve(await fn(...args));
      } catch (e) {
        reject(e);
      }
    };
    queue.push(task);
    // Try to start tasks ASAP (microtask ensures consistent ordering)
    queue.length && queue.length <= concurrency ? Promise.resolve().then(next) : next();
  });

  run.activeCount = () => active;
  run.pendingCount = () => queue.length;
  run.clearQueue = () => { queue.length = 0; };

  return run;
}

// // Example usage:
// const limit = pLimit(2);
// const wait = ms => new Promise(r => setTimeout(r, ms));
// await Promise.all([1,2,3,4,5].map(n => limit(async () => { await wait(100*n); return n; })));
