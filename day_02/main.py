from src.stat_engine import StatEngine
from src.monte_carlo import run_experiments
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

data = [3000, 5000, 7000, 120000, 4500, 6000, 8000, 150000]

engine = StatEngine(data)

print("Mean:", engine.get_mean())
print("Median:", engine.get_median())
print("Mode:", engine.get_mode())
print("Std Dev:", engine.get_standard_deviation())
print("Outliers:", engine.get_outliers())

print("\n--- Simulation ---")
run_experiments()