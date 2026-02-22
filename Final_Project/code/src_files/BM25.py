from rank_bm25 import BM25Okapi

# Add your import statements here

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD


class BM25():

  def __init__(self):
    self.docIDs = None
    self.reduced_matrix = None
    self.vectorizer = None
    self.svd = None
    self.bm25 = None
    

  def buildIndex(self, docs, docIDs, k, ngram):
    """
		Builds the document index in terms of the document
		IDs and stores it in the 'index' class variable

		Parameters
		----------
		arg1 : list
			A list of lists of lists where each sub-list is
			a document and each sub-sub-list is a sentence of the document
		arg2 : list
			A list of integers denoting IDs of the documents
		Returns
		-------
		None
		"""
    print("Using BM25 model evaluate relevance ...")

    joined_docs = []

    for doc in docs:
      list = []
      for sentence in doc:
        list.extend(sentence)
      joined_docs.append(list)
    
    bm25 = BM25Okapi(joined_docs)
    
    self.docIDs = docIDs
    self.bm25 = bm25

  def rank(self, queries):
    """
    Rank the documents according to relevance for each query
    
    Parameters
    ----------
    arg1 : list
      A list of lists of lists where each sub-list is a query and
      each sub-sub-list is a sentence of the query
      
    
    Returns
    -------
    list
      A list of lists of integers where the ith sub-list is a list of IDs
      of documents in their predicted order of relevance to the ith query
    """

    all_scores = []
    doc_IDs_ordered = []

    joined_queries = []
    for query in queries:
      list = []
      for sentence in query:
        list.extend(sentence)
      joined_queries.append(list)

    for query in joined_queries:
      scores = self.bm25.get_scores(query)
      all_scores.append(scores)
   
    

    for sim_score in all_scores:
      sim_scores = []
      for i in range(len(self.docIDs)):
        sim_scores.append((self.docIDs[i], sim_score[i]))

      sorted_list = sorted(sim_scores, key=lambda x: x[1], reverse=True)
      ranked = []

      for tuple in sorted_list:
        ranked.append(tuple[0])

      doc_IDs_ordered.append(ranked)  

    return doc_IDs_ordered
