import sys
import networkx as nx
import matplotlib.pyplot as plt
if __name__ == "__main__":
    """
    This code block is checking if the current file is being run as the main program. 
    If it is, it prints the name of the file and the first command line argument. 
    It then opens a file called "out.txt" and reads its contents into a variable called "path". 
    The contents of "path" are then split by commas into a list called "cities". 
    A new graph is created using the NetworkX library, and edges are added to the graph based on the cities in the "cities" list. 
    The nodes in the graph are colored red or blue based on their value. 
    Finally, the graph is drawn and saved as a PNG file called "path.png".
    """
    print(sys.argv[0])
    print(sys.argv[1])
    f = open("out.txt", "r")
    path = f.read()
    cities = path.split(",")
    print(cities)
    g = nx.Graph()
    for i in range(len(cities)-2):
        print(cities[i], cities[i+1])
        g.add_edge(cities[i], cities[i+1])
    node_colors = ["r" if node == 1 else "b" for node in g.nodes()]
    nx.draw(g, with_labels=True, node_shape="s",
            node_size=2000, node_color=node_colors)
    plt.savefig("path.png")
