import os
import spacy
nlp = spacy.load("en_core_web_sm")
import pandas as pd
import numpy
import matplotlib.pyplot as plt
from spacytextblob.spacytextblob import SpacyTextBlob
import argparse

def generate_scores(headlines):
    scores = []
    for headline_doc in nlp.pipe(headlines, batch_size=1000):
        for headline in headline_doc.sents:
            scores.append(headline._.sentiment.polarity)
    return scores

def create_rolling_means(dataframe): #To smooth the curves
    monthly = pd.DataFrame.copy(dataframe)
    monthly['score'] = monthly['score'].rolling(30).mean()
    weekly = pd.DataFrame.copy(dataframe)
    weekly['score'] = weekly['score'].rolling(7).mean()

    return monthly, weekly

def create_plot(weekly, monthly):
    plt.figure(figsize = (20, 10))
    plt.plot(weekly['date'], weekly['score'], label = 'Weekly')
    plt.plot(monthly['date'], monthly['score'], label = 'monthly')
    plt.title('Polarity scores for headlines')
    plt.xlabel('date')
    plt.ylabel('score')
    plt.legend()
    plt.savefig(os.path.join('output', 'output.png'))

def main(data_dir_path, is_sample):
    data = pd.read_csv(data_dir_path)
    if is_sample == 'true' or is_sample == 'True':
        headlines = data['headline_text'][:5000]
        dates = data['publish_date'][:5000]
    else:
        headlines = data['headline_text']
        dates = data['publish_date']

    nlp.add_pipe(SpacyTextBlob())
    
    scores = generate_scores(headlines)
    
    # Merge together the dates and the scores
    headlines_df = pd.DataFrame(zip(dates, scores), columns = ('date', 'score'))
    # As the amount of headlines per date is not consistent, pandas is used to group by dates
    headlines_df = headlines_df.groupby('date', as_index = False).mean()
    # Convert dates from strings to actual datetime objects. This will make sorting on dates easier.
    headlines_df['date'] = pd.to_datetime(headlines_df['date'], format = '%Y%m%d')

    monthly, weekly = create_rolling_means(headlines_df)

    create_plot(weekly, monthly)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Analyse the sentiment of headlines and generate rolling average plots based on that')
    parser.add_argument('-d', '--data_path', default = 'data/abcnews-date-text.csv')
    parser.add_argument('-s', '--is_sample', default = "false")

    args = parser.parse_args()

    main(data_dir_path = args.data_path, is_sample = args.is_sample)