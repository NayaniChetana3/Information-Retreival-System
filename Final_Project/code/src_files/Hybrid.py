# Add your import statements here

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

class Hybrid():

  def __init__(self):
    self.vectorizer = None
    self.tfidf_matrix = None
    self.docIDs = None
    self.transformer = None

  def buildIndex(self, docs, docIDs, k, ngram):

    print("Using VSM model to evaluate relevance...")
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

    joined_docs = []

    for doc in docs:
      list = []
      for sentence in doc:
        list.extend(sentence)
      joined_docs.append(list)
    #print(joined_docs)


    self.vectorizer = CountVectorizer(ngram_range=(x, y))
    freq_matrix= self.vectorizer.fit_transform([' '.join(sentence) for sentence in joined_docs])    #make sentences
    self.transformer = TfidfTransformer(norm='l2',use_idf=True, smooth_idf=False,sublinear_tf=False)
    self.transformer.fit(freq_matrix)
    tfidf_matrix = self.transformer.transform(freq_matrix)

    self.tfidf_matrix = tfidf_matrix
    self.index = tfidf_matrix.T
    #self.numOfDocs = len(docs)
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

    query_freq = self.vectorizer.transform(joined_queries)
    query_vectors = self.transformer.transform(query_freq)

    similarity_scores = cosine_similarity(query_vectors,self.tfidf_matrix)
        
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
