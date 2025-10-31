// topoSort.js
// Topological sort with cycle detection for dependency graphs.
// Accepts either: adjacency-list object or edge list. Throws on cycles.

/**
 * @typedef {Record<string,string[]>} Graph
 * @typedef {[string,string]} Edge  // [from, to]
 */

/**
 * Build adjacency list from edges or return copy of given graph.
 * @param {Graph|Edge[]} input
 * @returns {Graph}
 */
function toGraph(input) {
  /** @type {Graph} */
  const g = {};
  if (Array.isArray(input)) {
    for (const [u, v] of input) {
      if (!g[u]) g[u] = [];
      if (!g[v]) g[v] = [];
      g[u].push(v);
    }
  } else {
    for (const k of Object.keys(input)) g[k] = [...(input[k] || [])];
  }
  // Ensure all nodes appear
  for (const k of Object.keys(g)) for (const v of g[k]) if (!g[v]) g[v] = [];
  return g;
}

/**
 * Topologically sort nodes. Throws Error with cycle nodes if cyclic.
 * @param {Graph|Edge[]} input
 * @returns {string[]} order
 */
export function topoSort(input) {
  const g = toGraph(input);
  /** @type {Record<string,0|1|2>} */ // 0=unvisited,1=visiting,2=done
  const state = {};
  const order = [];
  const stack = [];

  const visit = (node) => {
    const st = state[node] || 0;
    if (st === 1) {
      // Found a back-edge → cycle is the suffix of the stack up to node
      const idx = stack.lastIndexOf(node);
      const cycle = stack.slice(idx).concat(node);
      const msg = `Cycle detected: ${cycle.join(" -> ")}`;
      const err = new Error(msg);
      // @ts-ignore attach for debugging
      err.cycle = cycle;
      throw err;
    }
    if (st === 2) return;

    state[node] = 1;
    stack.push(node);
    for (const nei of g[node]) visit(nei);
    stack.pop();
    state[node] = 2;
    order.push(node);
  };

  for (const node of Object.keys(g)) if (!state[node]) visit(node);
  return order.reverse();
}

/**
 * Group nodes by "level" (distance from sources) using Kahn's algorithm.
 * If graph has a cycle, throws like topoSort.
 * @param {Graph|Edge[]} input
 * @returns {string[][]} levels, where levels[0] are sources
 */
export function topoLevels(input) {
  const g = toGraph(input);
  const indeg = Object.fromEntries(Object.keys(g).map(k => [k,0]));
  for (const u of Object.keys(g)) for (const v of g[u]) indeg[v]++;

  /** @type {string[][]} */
  const levels = [];
  let layer = Object.keys(indeg).filter(k => indeg[k] === 0);

  let visited = 0;
  while (layer.length) {
    levels.push(layer);
    const next = [];
    for (const u of layer) {
      visited++;
      for (const v of g[u]) {
        if (--indeg[v] === 0) next.push(v);
      }
    }
    layer = next;
  }

  if (visited !== Object.keys(g).length) {
    // cycle present; derive one cycle path using DFS utility
    topoSort(g); // will throw with details
  }
  return levels;
}

// // Example usage:
// // const order = topoSort([["a","b"],["a","c"],["b","d"],["c","d"]]);
// // const levels = topoLevels({ a:["b","c"], b:["d"], c:["d"], d:[] });
