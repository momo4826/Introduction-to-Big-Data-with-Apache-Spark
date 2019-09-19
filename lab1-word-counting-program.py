#wordCount function
def wordCount(wordListRDD):
    wordPairs = wordListRDD.map(lambda x:(x,1)).reduceByKey(lambda x,y:x+y)
    return wordPairs
print wordCount(wordsRDD).collect()

#Capitalization and punctuation
import re
import string
def removePunctuation(text):
    text2= re.sub("[{}]+".format(string.punctuation),'',text)
    text3 =''
    for x in text2:
        text3 = text3 + x.lower()
    return text3.strip()
print removePunctuation('Hi, you!')
print removePunctuation(' No under_score!')

#Load a text file
import os.path
baseDir = os.path.join('data')
inputPath = os.path.join('cs100', 'lab1', 'shakespeare.txt')
fileName = os.path.join(baseDir, inputPath)

shakespeareRDD = (sc
                  .textFile(fileName, 8)
                  .map(removePunctuation))
print '\n'.join(shakespeareRDD
                .zipWithIndex()  # to (line, lineNum)
                .map(lambda (l, num): '{0}: {1}'.format(num, l))  # to 'lineNum: line'
                .take(15))

#Words from lines
shakespeareWordsRDD = shakespeareRDD.flatMap(lambda x:x.split(" "))#You might think that a map() transformation is the way to do this, but think about what the result of the split() function will be.

#Remove empty elements
shakeWordsRDD = shakespeareWordsRDD.filter(lambda x:len(x)!=0)
top15WordsAndCounts = wordCount(shakeWordsRDD).takeOrdered(15,lambda (x,y):-1*y)
print '\n'.join(map(lambda (w, c): '{0}: {1}'.format(w, c), top15WordsAndCounts))
