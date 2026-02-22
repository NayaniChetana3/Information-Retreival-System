
# Add your import statements here
from nltk.tokenize.treebank import TreebankWordTokenizer

class Tokenization():

  def naive(self, text):
    
    """
		Tokenization using a Naive Approach

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
	  """
    
		#Fill in code here
    #Words are separated based on the position of spaces
    
    tokenizedText = []
    for s in text:
      w = ''
      sent = []
      for c in s:
        if c != ' ':
          w += c
        else:
          sent.append(w.lower())
          w = ''
      if len(w) != 0:
        sent.append(w)
      tokenizedText.append(sent)
    return tokenizedText



  def pennTreeBank(self, text):
		
    """
		Tokenization using the Penn Tree Bank Tokenizer

		Parameters
		----------
		arg1 : list
			A list of strings where each string is a single sentence

		Returns
		-------
		list
			A list of lists where each sub-list is a sequence of tokens
		"""

    tokenizedText = []

	  #Fill in code here
    tokenizer = TreebankWordTokenizer()
    for sent in text:
      tokenizedText.append(tokenizer.tokenize(sent))
    return tokenizedText

		