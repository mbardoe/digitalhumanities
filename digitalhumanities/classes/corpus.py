from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt 

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

	def all_words(self):
		return word_tokenize(self.text, language=self.language)

	def words(self):
		filtered_text=''
		stopWords=self.stopwords()
		wordsFiltered=[]
		for w in words:
			if w.lower() not in stopWords:
				if w.isalpha():
					wordsFiltered.append(w.lower())
		# Rebuild text from a list of words. WordCloud likes one big string.
		for word in wordsFiltered:
			filtered_text=filtered_text+word+' '
		return filtered_text

	def stopwords(self):
		stopWords = stopwords.words('french')
		moreStopsFile=open('stopwords/'+self.language+'.dat', 'r')
		moreStops=moreStopsFile.read().split()
		stopWords=set(moreStops+stopWords)
		return stopWords

	def wordcloud(self):
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

	def show_occurences(self, substring, binWidth=100):
		occurances = find_substring(substring)
		plt.hist(occurances, bins=range(0, len(self.text)+binWidth, binWidth))

	def paragraphs(self):
		
		return 

