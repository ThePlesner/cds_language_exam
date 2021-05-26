import os
import csv
import pandas as pd
import spacy
from tqdm import tqdm
nlp = spacy.load('en_core_web_sm')
from itertools import combinations
from collections import Counter

def main(data_path):
    data = pd.read_csv(data_path)
    df = data[data['label'] == 'REAL']['text']

    # Extract named entities for 'person'
    entities = []
    for post in tqdm(df):
        # create temporary list
        temp_list = []
        # spacy doc object
        doc = nlp(post)
        
        for entity in doc.ents:
            if entity.label_ == 'PERSON':
                temp_list.append(entity.text)
        # append to the main list - it becomes a list of lists
        entities.append(temp_list)
    
    # using itertool that allows to to operations on list objects.
    # We want to create an edgelist from the entities
    edgelist = []
    for doc in entities:
        # using combinations to create possible pairs of entities
        edges = list(combinations(doc, 2))
        for edge in edges:
            edgelist.append(tuple(sorted(edge)))
    
    edgelist_path = os.path.join('edgelists', 'edgelist.csv')

    # Save the edgelist as a csv-file with the three columns. 
    with open(edgelist_path, 'w', encoding = 'utf8', newline = '') as output:
        writer = csv.writer(output)
        writer.writerow(['nodeA', 'nodeB', 'weight'])


        # Before writing to the csv we add weights to the edges
        for pair, weight in Counter(edgelist).items():
            nodeA = pair[0]
            nodeB = pair[1]
            writer.writerow([nodeA, nodeB, weight])



    

if __name__ == '__main__':
    main(os.path.join('data', 'fake_or_real_news.csv'))