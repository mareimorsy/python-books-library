import os

def readFile(fileName):
    if (os.path.exists(fileName)):
        with open(fileName, encoding = 'utf-8') as f:
            return f.read()
    else:
        return '[]'

def writeFile(fileName, text):
    if not (os.path.exists(fileName)):
        # create the file if it doesn't exist
        f = open(fileName, "x")
    with open(fileName,'w',encoding = 'utf-8') as f:
        f.write(text)

def deleteFile(fileName):
    os.remove(fileName)