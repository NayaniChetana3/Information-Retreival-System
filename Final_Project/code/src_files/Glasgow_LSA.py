# Add your import statements here

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
import math
from scipy.sparse import csr_matrix


class Glasgow_LSA():

  def __init__(self):
    self.docIDs = None
    self.reduced_matrix = None
    self.vectorizer = None
    self.svd = None
    

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
    print("Using Glasgow_LSA model using {} concepts to evaluate relevance...".format(k))
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
      joined_docs.append(' '.join(list))

    #count matrix
    self.vectorizer = CountVectorizer(ngram_range=(x,y))
    freq_matrix= self.vectorizer.fit_transform(joined_docs)    #make sentences

    vectorizer = TfidfVectorizer(ngram_range=(1,2))
    X = vectorizer.fit_transform(joined_docs)

    X = X.toarray()
    normal_mat = freq_matrix.toarray()

    unique_terms_doc = []
    for doc in joined_docs:
      words = doc.split()
      unique_terms = len(set(words))
      unique_terms_doc.append(unique_terms)

    for i in range(len(normal_mat)):
      for j in range(len(docIDs)):
        if normal_mat[i][j] != 0 and unique_terms_doc[j] >=2:
          idf = X[i][j]/normal_mat[i][j]
          den = math.log(int(unique_terms_doc[j]),10)
          num = math.log(int(normal_mat[i][j]) + 1,10)
          #print(den,num,idf)
          normal_mat[i][j] = (num*idf/den)
        else:
          normal_mat[i][j] = 0

    csr_mat = csr_matrix(normal_mat)
    svd = TruncatedSVD(n_components= k, random_state=42)
    reduced_matrix = svd.fit_transform(csr_mat)

    self.reduced_matrix = reduced_matrix
    self.docIDs = docIDs
    self.vectorizer = vectorizer
    self.svd = svd    
    self.docIDs = docIDs
    

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

    doc_IDs_ordered = []

    #Fill in code here
    joined_queries = []
    for query in queries:
      list = []
      for sentence in query:
        list.extend(sentence)
      joined_queries.append(' '.join(list))
    #print(joined_queries)

    query = self.vectorizer.transform(joined_queries)
    query_vectors = self.svd.transform(query)

    similarity_scores = cosine_similarity(query_vectors,self.reduced_matrix)
   
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
