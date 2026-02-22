# Add your import statements here

import nltk
from gensim import corpora, models, similarities
# Import necessary libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity

class LDA():

  def __init__(self):
    self.vectorizer = None
    self.lda_model = None
    self.X = None
    self.docIDs = None

  def buildIndex(self, docs, docIDs, k, ngram):

    print("Using LDA model to evaluate relevance...")
    joined_docs = []

    for doc in docs:
      list = []
      for sentence in doc:
        list.extend(sentence)
      joined_docs.append(' '.join(list))
    #print(joined_docs)
    x = 1
    y = 2
    if ngram == 1:
      x = 1
      y = 1
      print("Using unigram model to evaluate relevance...")
    elif ngram == 2:
      x = 2
      y = 2
      print("Using bigram model to evaluate relevance...")
    elif ngram == 1.5:
      x = 1
      y = 2
      print("Using hybrid model to evaluate relevance...")

    vectorizer = CountVectorizer(ngram_range=(x,y))
    X = vectorizer.fit_transform(joined_docs)

    lda_model = LatentDirichletAllocation(n_components=500, random_state=42)
    lda_model.fit(X)
    self.X = X
    self.lda_model = lda_model
    self.vectorizer = vectorizer
    self.docIDs = docIDs

  def rank(self, queries):

    doc_IDs_ordered = []

    #Fill in code here
    joined_queries = []
    for query in queries:
      list = []
      for sentence in query:
        list.extend(sentence)
      joined_queries.append(' '.join(list))
    #print(joined_queries)

    #joined_queries = [nltk.word_tokenize(query) for query in joined_queries]
    vectorizer = self.vectorizer
    lda_model = self.lda_model
    X = self.X

    query_transformed = lda_model.transform(vectorizer.transform(joined_queries))

    # Compute the similarity between the query and each document in the corpus
    similarity_scores = cosine_similarity(query_transformed, lda_model.transform(X))

    for sim_score in similarity_scores:
      sim_scores = []
      for i in range(len(self.docIDs)):
        sim_scores.append((self.docIDs[i], sim_score[i]))

      sorted_list = sorted(sim_scores, key=lambda x: x[1], reverse=True)
      ranked = []

      for tuple in sorted_list:
        ranked.append(tuple[0])

      doc_IDs_ordered.append(ranked)  

    return doc_IDs_ordered
