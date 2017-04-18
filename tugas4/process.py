import numpy as np
import re
from util import load_dataset, save_model, load_model
import sys
from nltk import RegexpParser, word_tokenize, pos_tag

with open("reviewdata.txt", "r") as dataset:

	#npchunking
	grammar = r"""
	  NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and noun
	      {<NNP>+}                # chunk sequences of proper nouns
	"""

	cp = RegexpParser(grammar)
	
	for sentence in dataset:
		words = word_tokenize(sentence)

		tagged_words = pos_tag(words)
		
		tree_result = cp.parse(tagged_words)

		for subtree in tree_result.subtrees():
			if subtree.label() == 'NP':
					print "%s | " % subtree

		print "\n"