# main.py
# This is the main file that:
#   1. Generates random arrays of different sizes
#   2. Measures execution time of Merge Sort and Quick Sort
#   3. Prints the results in the terminal
#   4. Plots a line graph and saves it as sorting_complexity.png

import sys           # To adjust the recursion limit

# ── Fix for Python 3.14: raise the recursion limit ──
# Python 3.14 uses a lower default recursion limit, which can cause
# a RecursionError inside matplotlib's font/text rendering code.
# We increase it here to prevent that error.
sys.setrecursionlimit(10000)

import time          # To measure execution time
import random        # To generate random integer arrays
import copy          # To copy arrays so both algorithms sort the same data

# ── Fix for Python 3.14: use the non-interactive 'Agg' backend ──
# The Agg backend renders plots to image files without opening a window.
# This avoids deep GUI-related call stacks that can trigger RecursionError
# on Python 3.14 when a display backend (like TkAgg) is used.
import matplotlib
matplotlib.use('Agg')  # Must be set BEFORE importing matplotlib.pyplot

import matplotlib.pyplot as plt  # To create the line graph

# Import our custom sorting algorithms from sorting.py
from sorting import merge_sort, quick_sort

# ─────────────────────────────────────────────
#  STEP 1: Define Input Sizes
# ─────────────────────────────────────────────

input_sizes = [10, 100, 1000]   # We will test for these three sizes

# Lists to store the measured times for each algorithm
merge_sort_times = []
quick_sort_times = []

# ─────────────────────────────────────────────
#  STEP 2: Generate Arrays, Sort, and Measure Time
# ─────────────────────────────────────────────

print("=" * 50)
print("   Sorting Complexity Visualizer")
print("   Compare: Merge Sort vs Quick Sort")
print("=" * 50)
print()

for n in input_sizes:
    # Generate a random array of 'n' integers (values between 1 and 10000)
    original_array = [random.randint(1, 10000) for _ in range(n)]

    # Make copies so both algorithms work on the exact same data
    array_for_merge = copy.copy(original_array)
    array_for_quick = copy.copy(original_array)

    # ── Measure Merge Sort time ──
    start_time = time.perf_counter()          # Start the timer
    merge_sort(array_for_merge)               # Run Merge Sort
    end_time = time.perf_counter()            # Stop the timer
    merge_time = end_time - start_time        # Calculate elapsed time
    merge_sort_times.append(merge_time)       # Save the time

    # ── Measure Quick Sort time ──
    start_time = time.perf_counter()          # Start the timer
    quick_sort(array_for_quick)               # Run Quick Sort
    end_time = time.perf_counter()            # Stop the timer
    quick_time = end_time - start_time        # Calculate elapsed time
    quick_sort_times.append(quick_time)       # Save the time

    # Print results for this input size
    print(f"Input Size (n = {n})")
    print(f"  Merge Sort Time : {merge_time:.8f} seconds")
    print(f"  Quick Sort Time : {quick_time:.8f} seconds")
    print()

# ─────────────────────────────────────────────
#  STEP 3: Print a Summary Table
# ─────────────────────────────────────────────

print("=" * 50)
print(f"{'n':<10} {'Merge Sort (s)':<20} {'Quick Sort (s)':<20}")
print("-" * 50)
for i, n in enumerate(input_sizes):
    print(f"{n:<10} {merge_sort_times[i]:<20.8f} {quick_sort_times[i]:<20.8f}")
print("=" * 50)
print()

# ─────────────────────────────────────────────
#  STEP 4: Plot the Line Graph
# ─────────────────────────────────────────────

# Create a figure with a specific size (width=8, height=5 inches)
plt.figure(figsize=(8, 5))

# Plot Merge Sort times — blue line with circle markers
plt.plot(input_sizes, merge_sort_times,
         color='blue',
         marker='o',
         linestyle='-',
         linewidth=2,
         markersize=8,
         label='Merge Sort')

# Plot Quick Sort times — red line with square markers
plt.plot(input_sizes, quick_sort_times,
         color='red',
         marker='s',
         linestyle='--',
         linewidth=2,
         markersize=8,
         label='Quick Sort')

# ── Labels and Title ──
plt.title('Sorting Algorithm Complexity: Merge Sort vs Quick Sort',
          fontsize=14, fontweight='bold')
plt.xlabel('Input Size (n)', fontsize=12)
plt.ylabel('Execution Time (seconds)', fontsize=12)

# ── Legend to identify each line ──
plt.legend(fontsize=11)

# ── Add a light grid for easier reading ──
plt.grid(True, linestyle='--', alpha=0.6)

# ── Make x-axis show exactly our input sizes ──
plt.xticks(input_sizes)

# ── Tight layout prevents labels from being cut off ──
plt.tight_layout()

# ── Save the graph as a PNG file ──
output_filename = 'sorting_complexity.png'
plt.savefig(output_filename, dpi=150)
print(f"Graph saved as '{output_filename}'")
print("Open 'sorting_complexity.png' in your file explorer to view the graph.")
