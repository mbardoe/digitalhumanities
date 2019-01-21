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

		language: A choice between "english" and "french".  Saved in __language__.

		"""

	def __init__(self, **kwargs):
		#self.__filename__=filename
		#self.__load_file__(self.__filename__)
		if not 'text' in kwargs.keys() and not 'filename' in kwargs.keys():
			raise TypeError("Must have a filename or text argument")
		if 'filename' in kwargs.keys():
			self.__load_file__(kwargs['filename'])
		if 'language' in kwargs.keys():
			self.language=kwargs['language']
		else:
			self.language='english'
		if 'text' in kwargs.keys():
			self.text=kwargs['text']


	
	def __load_file__(self, filename):
		myfile=open(self.__filename__, 'r')
		self.text=myfile.read()

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

