#get the name of the file or text and open it
name = input('Enter file:')
#to load files from .txt files, use - handle = open(name, 'r')
handle = open(name, 'r')
#handle = name

#count word frequency
counts = dict()
for line in handle:
  words = line.split()
  for word in words:
      counts[word] = counts.get(word,0) + 1

#find the most common word
bigCount = None
bigWord = None
for word, count in counts.items():
  if bigCount is None or count > bigCount:
    bigWord = word;
    bigCount = count;
    
#print the result
print(bigWord, bigCount)