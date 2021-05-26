import os
import csv
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm')
import networkx as nx
import matplotlib.pyplot as plt
import argparse


def main(edgelist_path, min_weight):
    with open(edgelist_path, 'r', encoding = 'utf8') as edgelist_csv:
        reader = csv.reader(edgelist_csv)
        # Remove headers
        edgelist = [tuple(row) for row in reader if tuple(row) != ('nodeA', 'nodeB', 'weight')]
        
        # Create dataframe from list
        df = pd.DataFrame(edgelist, columns = ['nodeA', 'nodeB', 'weight'])

        #Converting the entire 'weight'-column to actual integers
        df['weight'] = df['weight'].astype(int)
        
        # Filter using the min weight
        df = df[df['weight'] > min_weight]

        # Create a network from the read edgelist
        graph = nx.from_pandas_edgelist(df, 'nodeA', 'nodeB', ['weight'])

        # Using spring_layout as the pygraphviz caused problems.
        pos = nx.spring_layout(graph)
        
        # Drawing the network using the graph and some arguments to try and style the network just a little
        nx.draw_networkx(graph, pos, cmap = plt.get_cmap('jet'), node_size = 10, font_size = 5)
        nx.draw_networkx_edges(graph, pos)
        
        plt.savefig(os.path.join('viz', 'network.png'), dpi = 1000, bbox_inches = 'tight')

        # Centrality measures
        betweenness = nx.betweenness_centrality(graph)
        eigenvector = nx.eigenvector_centrality(graph)
        degree = graph.degree

        # Each measure gets its own dataframe to enable joining the data
        betweenness_df = pd.DataFrame(data = betweenness.items(), columns = ('node', 'betweenness'))
        eigenvector_df = pd.DataFrame(data = eigenvector.items(), columns = ('node', 'eigenvector'))
        degree_df = pd.DataFrame(data = degree, columns = ('node', 'degree'))

        # Combine into one dataframe
        # The three dataframes are joined on the node-column which is the label/name for a given node. 
        centrality_measures = betweenness_df.join(eigenvector_df.set_index('node'), on = 'node').join(degree_df.set_index('node'), on = 'node')
        centrality_measures.to_csv(os.path.join('output', 'measures.csv'))





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Creates a network based on a given edgelist')
    parser.add_argument('-e', '--edgelist_path', default = 'edgelists/edgelist.csv')
    parser.add_argument('-mw', '--min_weight', default = 300)
    args = parser.parse_args()

    main(args.edgelist_path, args.min_weight)