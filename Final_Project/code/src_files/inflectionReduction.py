# Add your import statements here
import nltk
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer

nltk.download('wordnet')


class InflectionReduction:

  def reduce(self, text):
    """
	  Stemming/Lemmatization

	  Parameters
		----------
		arg1 : list
		A list of lists where each sub-list a sequence of tokens
		representing a sentence

		Returns
		-------
		list
		A list of lists where each sub-list is a sequence of
		stemmed/lemmatized tokens representing a sentence
		"""

    reducedText = []
    reducedText2 = []
    #Fill in code here
    lemmatizer = WordNetLemmatizer()
    stemmer = PorterStemmer()

    for sent in text:
      reducedSent = []
      for w in sent:
        reducedSent.append(lemmatizer.lemmatize(w))
      reducedText.append(reducedSent)

    for sent in text:
      reducedSent = []
      for w in sent:
        reducedSent.append(stemmer.stem(w))
      reducedText2.append(reducedSent)
      
    return reducedText
