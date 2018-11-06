import numpy as np
import pandas as pd

train = pd.read_csv('twitbase.tsv', sep='\t')

tf1 = (train['text'][2:3]).apply(lambda x: pd.value_counts(x.split(" "))).sum(axis = 0).reset_index()
tf1.columns = ['words','tf']

for i,word in enumerate(tf1['words']):
  tf1.loc[i, 'idf'] = np.log(train.shape[0]/(len(train[train['text'].str.contains(word)])))

tf1['tfidf'] = tf1['tf'] * tf1['idf']

print(tf1)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer(max_features=1000, lowercase=True, analyzer='word',
 stop_words= 'english', ngram_range=(1,1))
train_vect = tfidf.fit_transform(train['text'])

print("TfIdf shape: ", train_vect.shape)
print(train_vect[1])