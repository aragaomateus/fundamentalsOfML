import streamlit as st
from pyvis.network import Network
import matplotlib.pyplot as plt
import numpy as np

# Generate a simple plot
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a network
network = Network(height="500px", width="100%", directed=True, notebook=False)

# Add nodes
network.add_node(1, label="Node 1")
network.add_node(2, label="Node 2")
network.add_node(3, label="Node 3")

# Add edges
network.add_edge(1, 2)
network.add_edge(2, 3)
network.add_edge(3, 1)

# Create a figure for the plot
fig, ax = plt.subplots()
ax.plot(x, y)

# Save the plot to a temporary file
temp_file = "temp_plot.png"
plt.savefig(temp_file)
plt.close(fig)

# Add the plot as a node in the network
network.add_node(4, label="Plot", shape='image', image=temp_file, size=1)

# Render the network
st.write(network.html, unsafe_allow_html=True)