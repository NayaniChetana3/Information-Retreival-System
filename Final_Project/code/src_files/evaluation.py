# Add your import statements here
import math


class Evaluation():

  def queryPrecision(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
    """
		Computation of precision of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The precision value as a number between 0 and 1
		"""

    #Fill in code here
    retrieved_doc = query_doc_IDs_ordered[:k]
    relnret = set(retrieved_doc).intersection(true_doc_IDs)
    precision = len(relnret) / k

    return precision

  def meanPrecision(self, doc_IDs_ordered, query_ids, qrels, k):
    """
		Computation of precision of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean precision value as a number between 0 and 1
		"""
    #Fill in code here

    precision_sum = 0
    for i in range(len(query_ids)):
      query_id = query_ids[i]
      doc_ids = doc_IDs_ordered[i]
      rel_docs = []
      for rel in qrels:
        if int(rel["query_num"]) == query_id:
          rel_docs.append(int(rel["id"]))

      precision_sum += self.queryPrecision(doc_ids, query_ids, rel_docs, k)

    meanPrecision = precision_sum / (len(query_ids))

    return meanPrecision

  def queryRecall(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
    """
		Computation of recall of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The recall value as a number between 0 and 1
		"""

    recall = -1

    #Fill in code here

    retrieved_doc = query_doc_IDs_ordered[:k]
    relnret = set(retrieved_doc).intersection(true_doc_IDs)
    recall = len(relnret) / len(true_doc_IDs)

    return recall

  def meanRecall(self, doc_IDs_ordered, query_ids, qrels, k):
    """
		Computation of recall of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean recall value as a number between 0 and 1
		"""

    meanRecall = -1

    #Fill in code here

    recall_sum = 0
    for i in range(len(query_ids)):
      query_id = query_ids[i]
      doc_ids = doc_IDs_ordered[i]
      rel_docs = []
      for rel in qrels:
        if int(rel["query_num"]) == query_id:
          rel_docs.append(int(rel["id"]))

      recall_sum += self.queryRecall(doc_ids, query_ids, rel_docs, k)

    meanRecall = recall_sum / (len(query_ids))

    return meanRecall

  def queryFscore(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
    """
		Computation of fscore of the Information Retrieval System
		at a given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The fscore value as a number between 0 and 1
		"""

    fscore = -1

    #Fill in code here
    retrieved_doc = query_doc_IDs_ordered[:k]
    relnret = set(retrieved_doc).intersection(true_doc_IDs)
    recall = len(relnret) / len(true_doc_IDs)
    precision = len(relnret) / k
    beta = 1
    if recall == 0 and precision == 0:
      fscore = 0
    else:
      fscore = ((beta*beta + 1) * recall * precision) / (recall + (beta*beta)*precision)

    return fscore

  def meanFscore(self, doc_IDs_ordered, query_ids, qrels, k):
    """
		Computation of fscore of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value
		
		Returns
		-------
		float
			The mean fscore value as a number between 0 and 1
		"""

    meanFscore = -1

    #Fill in code here
    f_sum = 0
    for i in range(len(query_ids)):
      query_id = query_ids[i]
      doc_ids = doc_IDs_ordered[i]
      rel_docs = []
      for rel in qrels:
        if int(rel["query_num"]) == query_id:
          rel_docs.append(int(rel["id"]))

      f_sum += self.queryFscore(doc_ids, query_id, rel_docs, k)

    meanFscore = f_sum / (len(query_ids))

    return meanFscore

  def queryNDCG(self, query_doc_IDs_ordered, query_id, true_doc_IDs, k):
    """
		Computation of nDCG of the Information Retrieval System
		at given value of k for a single query

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of IDs of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The nDCG value as a number between 0 and 1
		"""

    nDCG = -1

    #Fill in code here
    DCG = 0
    for i in range(1, k + 1):
      doc_id = query_doc_IDs_ordered[i - 1]
      logv = math.log(i + 1, 2)
      relv = true_doc_IDs.get(doc_id, 0)
      DCG += relv / logv

    rel_vals = []

    for doc in true_doc_IDs:
      rel_vals.append(true_doc_IDs[doc])

    rel_vals.sort(reverse=True)

    IDCG = 0
    for i in range(1, min(k + 1, len(rel_vals) + 1)):
      logv = math.log(i + 1, 2)
      relv = rel_vals[i - 1]
      IDCG += relv / logv

    if IDCG == 0:
      nDCG = 0
    else:
      nDCG = DCG / IDCG

    return nDCG

  def meanNDCG(self, doc_IDs_ordered, query_ids, qrels, k):
    """
		Computation of nDCG of the Information Retrieval System
		at a given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries for which the documents are ordered
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The mean nDCG value as a number between 0 and 1
		"""
    meanNDCG = -1

    sum_NDCG = 0

    for i in range(0, len(query_ids)):

      query_id = query_ids[i]
      docs_id = doc_IDs_ordered[i]
      rel_docs = {}
      for rel in qrels:
        if int(rel["query_num"]) == query_id:
          rel_docs[int(rel["id"])] = 5 - rel["position"]

      sum_NDCG += self.queryNDCG(docs_id, query_id, rel_docs, k)

    meanNDCG = sum_NDCG / len(query_ids)
    #Fill in code here
    return meanNDCG

  def queryAveragePrecision(self, query_doc_IDs_ordered, query_id,
                            true_doc_IDs, k):
    """
		Computation of average precision of the Information Retrieval System
		at a given value of k for a single query (the average of precision@i
		values for i such that the ith document is truly relevant)

		Parameters
		----------
		arg1 : list
			A list of integers denoting the IDs of documents in
			their predicted order of relevance to a query
		arg2 : int
			The ID of the query in question
		arg3 : list
			The list of documents relevant to the query (ground truth)
		arg4 : int
			The k value

		Returns
		-------
		float
			The average precision value as a number between 0 and 1
		"""
    avgPrecision = 0

    #Fill in code here
    count = 0
    for kVal in range(1, k + 1):
      if query_doc_IDs_ordered[kVal - 1] in true_doc_IDs:
        count += 1
        avgPrecision += self.queryPrecision(query_doc_IDs_ordered, query_id,
                                            true_doc_IDs, kVal)

    if count == 0:
      avgPrecision = 0
    else:
      avgPrecision = avgPrecision / count

    return avgPrecision

  def meanAveragePrecision(self, doc_IDs_ordered, query_ids, q_rels, k):
    """
		Computation of MAP of the Information Retrieval System
		at given value of k, averaged over all the queries

		Parameters
		----------
		arg1 : list
			A list of lists of integers where the ith sub-list is a list of IDs
			of documents in their predicted order of relevance to the ith query
		arg2 : list
			A list of IDs of the queries
		arg3 : list
			A list of dictionaries containing document-relevance
			judgements - Refer cran_qrels.json for the structure of each
			dictionary
		arg4 : int
			The k value

		Returns
		-------
		float
			The MAP value as a number between 0 and 1
		"""
    meanAveragePrecision = 0

    #Fill in code here
    for i in range(0, len(query_ids)):
      query_id = query_ids[i]
      doc_ids = doc_IDs_ordered[i]
      rel_docs = []
      for rel in q_rels:
        if int(rel["query_num"]) == query_id:
          rel_docs.append(int(rel["id"]))
      meanAveragePrecision += self.queryAveragePrecision(
        doc_ids, query_id, rel_docs, k)

    meanAveragePrecision = meanAveragePrecision / len(query_ids)
    return meanAveragePrecision
