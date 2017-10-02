# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30  2017

@author: Aboozar Mapar
@email: A.Mapar@gmail.com

Goal: Assess algorithmic knowledge.

Build order: You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

EXAMPLE

Input:

projects: a, b, c, d, e, f

dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)

Output:

f, e, a, b, d, c

Use any language you like for this one.




This code finds a build order for pairs of depended projects.
"""

import networkx as nx


"""
This function recursively looks for dependent projects and adds them to the varialbe
Order.

Input :: A directed graph
Output :: And ordered list of projects
"""
def find_order(Graph):
#    import networkx as nx
    
    # initializing varialbles
    Order =[]
    independent = []
    
    # finding independent projects
    for node in Graph.nodes():
        if len(Graph.successors(node))==0 and len(G.in_edges(node)) == 0:
            independent.extend(node)
    # removing independent projects from the graph
    Graph.remove_nodes_from(independent)
    
    # finding dependencies
    for node in Graph.nodes():
        if len(Graph.successors(node))==0 and len(G.in_edges(node)) > 0:
            Order.extend(node)
            Graph.remove_node(node)

    # adding the indepent projects to after the outter most dependent projects
    Order.extend(independent) 
    
    # If there are still nodes in the graph and there are some independent nodes.
    # If  out degree of a node is 0 it is not dependent on other nodes and can be 
    # safely removed from the graph.
    if len(Graph.nodes()) > 0 and 0 in Graph.out_degree().values():
            Order.extend(find_order(Graph))
           
    return Order






# Initialize the graph
G=nx.DiGraph()

# Adding projects
G.add_nodes_from(["a","b","c","d","e", "f"])

# Defining dependencies
G.add_edges_from([("a","d"),("f","b"),("b","d"),("f","a"),("d","c")])

# Reversing the graph so that the order second project in the above list is dependent on the  first project  
G=G.reverse()

# Visualizing the graph
# nx.draw(G, with_labels=True)

# Number of projects with in the graph
numNodes = G.number_of_nodes()

# Finding the build order
Build_Order = find_order(G)

if len(Build_Order) == numNodes :
    print "Build the projects in the following order :"
    print ' '.join(Build_Order)
else:
    print "Error! No valid build order can be found."
    


