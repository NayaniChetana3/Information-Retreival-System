import math


class Baseline():

  def __init__(self):
    self.index = None
    self.numOfDocs = None
    self.idf = None
    self.docIDs = None
    self.doc_map = None

  def buildIndex(self, docs, docIDs,k, ngram):
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
    index = {}

    #Fill in code here
    for i in range(len(docs)):
      curr_doc = docs[i]
      curr_id = docIDs[i]
      for sentence in curr_doc:
        for word in sentence:
          word_freq = index.get(word)
          if word_freq == None:
            index[word] = {curr_id: 1}
          else:
            curr_freq = word_freq.get(curr_id, 0)
            index[word][curr_id] = curr_freq + 1

    idf = {}
    for terms in index:
      idf[terms] = math.log((len(docs) / len(index.get(terms, {}))), 10)
    '''word_map[docId] = tf*idf of a word in a doc'''
    '''#smoothing
    for word in index:
      for doc in docIDs:
        if index[word].get(doc) == None:
          index[word][doc] = 1
        else:
          index[word][doc] += 1'''

    #tf*idf
    for word in index:
      word_map = index[word]
      for docId in word_map:
        index[word][docId] = word_map[docId] * idf[word]

    doc_map = {}  #doc -> denom
    for word in index:
      for docId in index[word]:
        val = index[word][docId]

        if doc_map.get(docId) == None:
          doc_map[docId] = val * val
        else:
          doc_map[docId] += val * val

    self.idf = idf
    self.index = index
    self.numOfDocs = len(docs)
    self.docIDs = docIDs
    self.doc_map = doc_map

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

    idf = self.idf
    for query in queries:
      word_map = {}

      for sentence in query:
        for word in sentence:
          word_freq = word_map.get(word, 0)
          word_map[word] = word_freq + 1   

      qval = 0
      for word in word_map:
        word_map[word] = word_map.get(word, 0) * idf.get(word, 0)
        qval += word_map[word]*word_map[word]
      '''word_map[word] = tf*IDF in a query'''

      
      
      dot_prods = []
      for doc in self.docIDs:
        sim = 0

        for sentence in query:
          for word in sentence:
            sim += word_map[word] * self.index.get(word, {}).get(doc, 0)

        if self.doc_map.get(doc, 0)*qval == 0:
          sim = 0
        else:
          sim = sim / math.sqrt(self.doc_map[doc]*qval)

        dot_prods.append((doc, sim))

      sorted_list = sorted(dot_prods, key=lambda x: x[1], reverse=True)
      ranked = []
      for tuple in sorted_list:
        ranked.append(tuple[0])

      doc_IDs_ordered.append(ranked)

    return doc_IDs_ordered
