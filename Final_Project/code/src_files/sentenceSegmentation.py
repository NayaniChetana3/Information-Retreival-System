# Add your import statements here
import nltk
nltk.download('punkt')

class SentenceSegmentation():
  
  def naive(self, text):
	  
    """
	  Sentence Segmentation using a Naive Approach

	  Parameters
	  ----------
	  arg1 : str
	  A string (a bunch of sentences)
	  Returns
	  -------
	  list
	  A list of strings where each string is a single sentence
    """
   
    #Fill in code here
    #Sentences are separated based on the positions of comma ',', period '.' and question mark '?'
    segmentedText = []
    text = text.strip()
    sent = ''
    for c in text:
      if c != ',' and c != '.' and c != '?' :
        sent += c
      else:
        segmentedText.append(sent)
        sent = ''
    if len(sent) != 0:
      segmentedText.append(sent)  
    return segmentedText


  def punkt(self, text):
		
    """
		Sentence Segmentation using the Punkt Tokenizer

		Parameters
		----------
		arg1 : str
			A string (a bunch of sentences)

		Returns
		-------
		list
			A list of strings where each strin is a single sentence
		"""

    segmentedText = None

		#Fill in code here
    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    segmentedText = tokenizer.tokenize(text.strip())
    return segmentedText