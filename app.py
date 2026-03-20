import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="ACO Optimisation", layout="wide")
st.title("ACO vs MMAS")
st.write("Comparison of Ant System and Max-Min Ant System for TSP")

st.sidebar.header("Algorithm Parameters")
alpha = st.sidebar.slider("Alpha (Pheromone Importance)", 0.0, 5.0, 1.0)
beta = st.sidebar.slider("Beta (Heuristic Importance)", 0.0, 5.0, 2.0)
rho = st.sidebar.slider("Rho (Evaporation Rate)", 0.0, 1.0, 0.1)
iterations = st.sidebar.number_input("Iterations", min_value=1, max_value=200, value=50)

dist_matrix = np.array([
    [0, 10, 12, 11, 14],
    [10, 0, 13, 15, 8],
    [12, 13, 0, 9, 14],
    [11, 15, 9, 0, 16],
    [14, 8, 14, 16, 0]
])
cities = ['A', 'B', 'C', 'D', 'E']

def calculate_dist(tour):
    d = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))
    return d + dist_matrix[tour[-1], tour[0]]

def run_simulation(mode):
    num_cities = 5
    num_ants = 5
    tau = np.full((5,5), 2.0) if mode == "MMAS" else np.ones((5,5))
    history = []
    best_dist = float('inf')
    
    for _ in range(iterations):
        iter_distances = []
        for ant in range(num_ants):
            curr = np.random.randint(5)
            tour, visited = [curr], {curr}
            while len(visited) < 5:
                eta = 1.0 / (dist_matrix[curr, :])
                p = (tau[curr, :]**alpha) * (eta**beta)
                p[[list(visited)]] = 0
                p /= p.sum()
                curr = np.random.choice(range(5), p=p)
                tour.append(curr)
                visited.add(curr)
            
            d = calculate_dist(tour)
            iter_distances.append(d)
            if d < best_dist: best_dist = d
            
        tau *= (1 - rho)
        if mode == "AS":
            for d in iter_distances: tau += (1/d)
        else: 
            tau += (1/best_dist)
            tau = np.clip(tau, 0.1, 2.0)
        history.append(best_dist)
    return history

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Distance Matrix")
    st.table(pd.DataFrame(dist_matrix, columns=cities, index=cities))

with col2:
    if st.button("Run Comparison"):
        as_res = run_simulation("AS")
        mmas_res = run_simulation("MMAS")
        
        fig, ax = plt.subplots()
        ax.plot(as_res, label="Ant System", color="#3498db")
        ax.plot(mmas_res, label="Max-Min Ant System", color="#e74c3c", linestyle="--")
        ax.set_ylabel("Shortest Distance")
        ax.set_xlabel("Iteration")
        ax.legend()
        st.pyplot(fig)
        
        st.success(f"Best Distance Found: {min(mmas_res)}")

#st.info("💡 Tip: Try increasing Beta to see how ants prioritize nearby cities immediately!")