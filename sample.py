import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import json
import warnings

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title("Graph Network Database Visualization")

# Load data from JSON file
try:
    with open("data.json") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}

# Create graph
G = nx.Graph()
for person, info in data.items():
    G.add_node(person, job=info['Job'])
    for connection in info['Connections']:
        G.add_edge(person, connection)

# Plot graph with job information on hover
pos = nx.spring_layout(G)
labels = {node: node + "\n" + data[node]['Job'] for node in G.nodes()}
nx.draw(G, pos, with_labels=False)
nx.draw_networkx_labels(G, pos, labels)

# Show plot in Streamlit app
st.pyplot()

# Add a person form
add_person = st.checkbox("Add a person to the database")
if add_person:
    new_person = st.text_input("Enter the name of the person:")
    new_job = st.text_input("Enter the job of the person:")
    if st.button("Submit"):
        data[new_person] = {'Job': new_job, 'Connections': []}
        G.add_node(new_person, job=new_job)
        st.success("Person added to the database!")

# Add a connection form
add_connection = st.checkbox("Add a connection between two people")
if add_connection:
    person1 = st.text_input("Enter the name of the first person:")
    person2 = st.text_input("Enter the name of the second person:")
    if st.button("Submit"):
        if person1 in data and person2 in data:
            data[person1]['Connections'].append(person2)
            data[person2]['Connections'].append(person1)
            G.add_edge(person1, person2)
            st.success("Connection added between {} and {}!".format(person1, person2))
        else:
            st.error("One or both of the people not found in the database.")

# Write updated data to JSON file
with open("data.json", "w") as f:
    json.dump(data, f)

import streamlit as st
from pyvis.network import Network

# Create a network
network = Network(height="500px", width="100%", directed=True)

# Add nodes
network.add_node(1, label="Node 1")
network.add_node(2, label="Node 2")
network.add_node(3, label="Node 3")

# Add edges
network.add_edge(1, 2)
network.add_edge(2, 3)
network.add_edge(3, 1)

# Render the network
st.write(network.html, unsafe_allow_html=True)
# Update plot with new information
plt.clf()
