# Simple Script for Finding Most Popular Word In My Writing

# Collect Files From a Folder (Text Files)
import os
directory = os.listdir(os.getcwd())

#Our Dictionary
dictionary = {}

# Read Through Each File and Make List of Most Used Words
for file in directory:
    #Only open the file if it is a text File
    if file.endswith('.txt'):

    #Open the file
        with open(file, 'r') as currentFile:
            text = currentFile.read()
            listOfWords = text.split()

            # Add Words to Dictionary
            for word in listOfWords:
                #if the word already exists in our dictionary increment value of keypair
                if dictionary.get(word):
                    previousValue = dictionary.get(word)
                    newValue = previousValue+1
                    dictionary[word] = newValue
                #if the word is not in our dictionary we want to add key and give a value of 1
                else: dictionary[word] = 1

#print(dictionary)
sortedDict = sorted(dictionary.items(), reverse = True)
print(sortedDict)
