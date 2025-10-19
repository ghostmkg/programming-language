#!/usr/bin/env python3
#hacktoberfest contributions visualization - Golixco
"""
Simple Hacktoberfest contributions visualization

This script simulates daily contribution counts for a month (e.g. October)
and plots a bar chart for daily contributions plus a cumulative line so you
can see progress over the month. Replace the simulated data with real data
if you want to visualize your actual contributions.
"""
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

# reproducible pseudo-random demo data
np.random.seed(42)

# choose the month and year to label the chart (you can change these)
year = 2025
month = 10  # October (Hacktoberfest)

# number of days (simple approach, assume 31 days for the demo)
days = np.arange(1, 32)

# simulate daily contributions: mostly small numbers but occasional spikes
daily = np.random.poisson(lam=1.8, size=len(days))
# add a few spikes to simulate PR/issue events on certain days (human-like touch)
daily[[3, 10, 18, 24]] += np.array([2, 3, 4, 2])

# cumulative contributions
cum = np.cumsum(daily)

# create figure (single plot)
fig, ax = plt.subplots(figsize=(11, 5))

# bar chart for daily contributions
ax.bar(days, daily)

# overlay cumulative as a line on the same axes (make it visible without custom colors)
ax.plot(days, cum, marker='o')

# labels and title
ax.set_xlabel("Day of October")
ax.set_ylabel("Number of contributions")
ax.set_title("Simulated Hacktoberfest Contributions — Daily & Cumulative")

# small tidy-up for ticks and grid
ax.set_xticks(days[::2])  # show every other day to avoid clutter
ax.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.6)

# annotate last cumulative value (small human-style touch)
last_val = cum[-1]
ax.annotate(f"Total: {last_val}", xy=(days[-1], last_val),
            xytext=(-60, 10), textcoords="offset points")

# save and show
plt.tight_layout()
plt.savefig("hacktoberfest_contributions.png")
print("Saved plot to hacktoberfest_contributions.png")
plt.show()
