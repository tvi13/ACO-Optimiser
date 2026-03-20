## Evolutionary Computing: ACO vs MMAS

The project focuses on solving the Travelling Salesman Problem (TSP) using two variants of Ant Colony Optimization:

1. Ant System (AS): The original algorithm where all ants contribute to pheromone updates.

2. Max-Min Ant System (MMAS): An improved version that restricts updates to the best ant and bounds pheromone values to prevent stagnation.

**Experiment Objectives**

1. Implement the Ant System (AS) Algorithm on a 5×5 TSP distance matrix.

2. Apply the Max-Min Ant System (MMAS) Algorithm on the same problem.

3. Compare and analyze both algorithms in terms of convergence, time, and complexity.

**Project Structure**

1. app.py: A Streamlit-based interactive dashboard to visualize the optimization process.

2. requirements.txt: List of Python dependencies required to run the project.

**Algorithm Comparison**

1. Ant System (AS): Uses a positive feedback process where ants deposit pheromones proportional to the quality of their tour.

2. Max-Min Ant System (MMAS): Limits pheromones between the min and max values to ensure exploration and relies only on the global_best ant for updates
