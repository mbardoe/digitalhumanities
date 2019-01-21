from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt 
from wordcloud import WordCloud
import os
from .tools import find_substring

class Corpus(object):
	"""A class that represents a body of writing. This class implements a
	variety of tools that will be useful for investigating the qualities of 
	this text and comparing the text to other texts. 

	Args:
		filename: the path to a utf-8 text file where paragraphs are delimited 
		with "\n\n". This information is saved in __filename__.

		text: a string that defines the corpus. Use text or filename.

		language: A choice between "english" and "french".  \

		"""

	def __init__(self, filename, language='english'):
		myfile=open(filename, 'r')
		self.text=myfile.read()
		self.language=language
		#print(os.path)

	def all_words(self):
		"""Returns a list of all the words tokenized in the text.
			
			Returns: list of of tokenized words
		"""
		return word_tokenize(self.text, language=self.language)

	#def path(self):
	#	print(os.path)

	def words(self):
		filtered_text=''
		stopWords=self.stopwords()
		wordsFiltered=[]
		for w in self.all_words():
			if w.lower() not in stopWords:
				if w.isalpha():
					wordsFiltered.append(w.lower())
		# Rebuild text from a list of words. WordCloud likes one big string.
		for word in wordsFiltered:
			filtered_text=filtered_text+word+' '
		return filtered_text

	def stopwords(self):
		"""Collects the stopwords for the language associted with this corpus.

        Returns:	A set of stopwords

        """
		basepath = os.path.dirname(os.path.abspath(__file__))
		parentpath = os.path.dirname(os.path.dirname(basepath))
		stopwordspath = parentpath + '/digitalhumanities/classes/stopwords/' + self.language +'.dat'
		stopWords = stopwords.words('french')
		moreStopsFile=open(stopwordspath, 'r')
		moreStops=moreStopsFile.read().split()
		stopWords=set(moreStops+stopWords)
		return stopWords

	def wordcloud(self):
		"""Creates a word cloud based ont the corpus.
        
        """
		wordcloud = WordCloud(width = 800, height = 800,
                background_color ='white',
                min_font_size = 10).generate(self.words())
		plt.figure(figsize = (8, 8), facecolor = None)
		plt.imshow(wordcloud)
		plt.axis("off")
		plt.tight_layout(pad = 0)
		plt.show() 

	def find_substring(self,substring):
		return find_substring(substring, self.text)

	def show_occurences(self, substring, binWidth=-1):
		"""Shows a bar plot of the occurances of the substring in the text.
		The x-axis is the position in the text as measured in characters.

        """

		length=len(self.text)
		if binWidth==-1:
			binWidth=int(length/40)
		occurances = find_substring(substring, self.text)
		plt.hist(occurances, bins=range(0, len(self.text)+binWidth, binWidth))

	def paragraphs(self):
		
		return 

