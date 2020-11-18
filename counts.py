from santize import sanitize

#spaces is bool
def charcount(file ,spaces=True):
    text = file.read()
    if spaces == False:
        text = text.replace(" ", "")
    return len(text)

def linecount(file):
    return len(file.readlines())

#count question marks, exclamation points, and apostrophes
def specialcount(file):
    specialdict = {"apostrophe": 0, "question": 0, "exclamation": 0, "semicolon": 0}

    for char in file.read():
        if char == "'":
            specialdict["apostrophe"] += 1
        if char == "?":
            specialdict["question"] += 1
        if char == "!":
            specialdict["exclamation"] += 1
        if char == ";":
            specialdict["semicolon"] += 1
    
    return specialdict

def wordcount(file):
    text = file.readlines()
    words = 0
    for line in text:
        words += len(sanitize(line).split())
    return words