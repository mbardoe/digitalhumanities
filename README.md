# digitalhumanities

The goal of this class is to create wrapper functions for various '''nltk''' and other libraries to make explanatory data analysis of texts in English and french more easily done within a Jupyter notebook. Some functionality that I would like to see:

* The ability to take a text, and in a single line create a word cloud.
* Easily create data displays of substring frequency in the text. 
* Show distribution of paragraph and sentence length.
* Easily show the the word frequencies in the text.
* Determine the grade level of various texts.

## Example

Below you will see some examples of how the functions can be used with. The
goal is that these functions would be easily used in a Jupyter notebook for 
easy analysis

```
import digitalhumanities
etrangfr=digitalhumanities.Corpus("texts/etrangerfr.txt", 'french')
etrangfr.wordcloud()
```
![Wordcloud for the french version of The Stranger][etrangerfr]
```
etrenglish.show_occurences("?")
```
![Graphs show question marks in English translation of The Stranger][etrenglishQuestion]





[etrangerfr]: https://github.com/mbardoe/digitalhumanities/blob/master/images/wordcloudetrangerfr.png

[etrenglishQuestion]: https://github.com/mbardoe/digitalhumanities/blob/master/images/etrengishQuestionocc.png