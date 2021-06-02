import os
import random as rn
import shutil

listOfWords = ['benign', 'malignant']
listOfFiles = {'train': [],
               'validation': [],
               'test': []}
rn.seed(443)
for word in listOfWords:
    directory = word+'_224_224'
    filesInDirectory = os.listdir(directory)
    nbrOfFiles = len(filesInDirectory)
    
    # First pick by 80%, then split by 50%, and then the rest
    # This makes 80%/10%/10%
    setSizes = {'train': 0.8, 'test': 0.5,'validation': 1.0}
    for setName, percentage in setSizes.items():
        tmpList = rn.sample(filesInDirectory, int(len(filesInDirectory)*percentage))
        print(nbrOfFiles, len(tmpList))
        # Copy files
        filesInDirectory = [x for x in filesInDirectory if not x in tmpList]
        
        # This is performing the copy
        cpFiles = [shutil.copyfile(directory + '/' + y, setName + '_224_224/' + directory.split('_')[0] + '/' + y) for y in tmpList]
        print("Target folder:", setName, '\n')
        
        