import os
from pprint import pprint
import json
import argparse
from pathlib import Path
import pandas as pd
import seaborn as sns

from matplotlib import rcParams
rcParams['figure.figsize'] = 20,10 # figure size

import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel

# Utils from class
from utils import lda_utils

import spacy
nlp = spacy.load("en_core_web_sm", disable=["ner"])


# for response in the terminal
import logging, warnings
warnings.filterwarnings('ignore')
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.ERROR)

def main(data_path, topic_num):
    outpath = 'output'
    # Load dataset and convert from json to python dictionary
    with open(data_path) as file:
        content = file.read()
        line_dict = json.loads(content)

    # Concatenates all lines said in each star trek series by spaces
    # so it will be represented as one doc
    episodes = {}
    for series_name, series in line_dict.items():
        for episode_name, episode in series.items():
            episode_string = ''

            for character_lines in episode.values():
                lines = ' '.join(character_lines)
            
                # Avoid empty lines
                if len(lines) != 0:
                    episode_string += ' ' + lines

            # Add the string containing all lines from the episode to our dict
            episode_key = series_name + '_' + episode_name.split()[1]
            episodes[episode_key] = episode_string

    # Convert lines to a list for gensim processing
    episode_lines = list(episodes.values())

    # Build the bigram and trigram models
    # A higher threshold results in fewer phrases
    bigram = gensim.models.Phrases(episode_lines, min_count=10, threshold=80)
    trigram = gensim.models.Phrases(bigram[episode_lines], threshold=80)  
    bigram_mod = gensim.models.phrases.Phraser(bigram)
    trigram_mod = gensim.models.phrases.Phraser(trigram)

    # tokenize words and clean the lines for stopwords
    # We found that using only nouns worked the best
    processed_lines = lda_utils.process_words(episode_lines, nlp, bigram_mod, trigram_mod, allowed_postags=["NOUN"])

    # convert to id's
    id2word = corpora.Dictionary(processed_lines)

    # Count frequencies of ids collocation for each episode
    corpus = [id2word.doc2bow(episode_lines) for episode_lines in processed_lines]

    # LDA model
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                            id2word=id2word,num_topics=topic_num, 
                                            random_state=1111,
                                            chunksize=10,
                                            passes=10,
                                            iterations=100,
                                            per_word_topics=True, 
                                            minimum_probability=0.0)

    # Compute Perplexity
    metrics = f'Perplexity: {lda_model.log_perplexity(corpus)}' # the lower the better

    # Compute Coherence Score
    coherence_model_lda = CoherenceModel(model=lda_model, 
                                        texts=processed_lines, 
                                        dictionary=id2word, 
                                        coherence='c_v')

    coherence_lda = coherence_model_lda.get_coherence()
    metrics += f'\nCoherence Score: {coherence_lda}'
    print() # newline
    print(metrics)

    # Topic overview
    topics = lda_model.print_topics()
    print() # newline
    # pretty data print
    pprint(topics)

    # Save metrics and topics
    with open(os.path.join(outpath, 'metrics_and_topics.txt'), 'w') as file:
        file.write(metrics + '\n\n' + str(topics))

    # Generate a plot of topics in episodes
    values = list(lda_model.get_document_topics(corpus))

    split = []
    for entry in values:
        topic_prevelance = []
        for topic in entry:
            topic_prevelance.append(topic[1])
        split.append(topic_prevelance)

    df = pd.DataFrame(map(list,zip(*split)))

    # Smooth the curve with rolling mean
    topic_plot = sns.lineplot(data=df.T.rolling(20).mean())
    topic_plot.figure.savefig(os.path.join(outpath, 'topics.png'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "do topic analysis of Star Trek episodes")
   
    parser.add_argument("-d", "--data_path", type = Path, default = Path('./data/all_series_lines.json'), help = "the path to the Star Trek json data file")
    parser.add_argument("-t", "--topic_num", default = 12, type = int, help = "the number of topics to identify in the Star Trek episodes")

    args = parser.parse_args()
    
    main(data_path = args.data_path, topic_num = args.topic_num)