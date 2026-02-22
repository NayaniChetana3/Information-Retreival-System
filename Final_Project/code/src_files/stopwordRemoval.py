
# Add your import statements here
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

class StopwordRemoval():

  def fromList(self, text):
		
    """
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
			representing a sentence with stopwords removed
		"""

    stopwordRemovedText = []

		#Fill in code here
    stop_words = set(stopwords.words('english'))
    stopwordRemovedText = []
    for sent in text:
      stopWordRemovedSent = []
      for w in sent:
        if not w.lower() in stop_words:
          stopWordRemovedSent.append(w)
      stopwordRemovedText.append(stopWordRemovedSent)
    return stopwordRemovedText




	