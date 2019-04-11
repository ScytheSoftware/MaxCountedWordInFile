#DaVonte' Whitfield 
#Python
#You can upload a file and this program will count all words and output the highest word with the amount.
import operator

counts = dict()
bodyOfText = open('EnterTextFileHere.txt', 'r')  #Load a txt file here.

corpus = bodyOfText.read()
words = corpus.split()  #Turn into an array.


for word in words:  # Select each word in the collection of words.
	counts[word] = counts.get(word, 0) +1

print("")
print(counts)
print("")


print("The max counted word:'",max(counts.items(), key=operator.itemgetter(1))[0], "'/ Number of times:", counts.get(max(counts.items(), key=operator.itemgetter(1))[0]))

		
