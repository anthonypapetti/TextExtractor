from sanitize import sanitize

#spaces is bool
def charcount(text,spaces=True):
    if spaces == False:
        text = text.replace(" ", "")
    return len(text)

#count question marks, exclamation points, and apostrophes
def specialcount(text):
    specialdict = {"apostrophe": 0, "question": 0, "exclamation": 0, "semicolon": 0}

    for char in text:
        if char == "'":
            specialdict["apostrophe"] += 1
        if char == "?":
            specialdict["question"] += 1
        if char == "!":
            specialdict["exclamation"] += 1
        if char == ";":
            specialdict["semicolon"] += 1
    
    return specialdict

def linecount(text):
    return len(text.split("\n"))

def wordcount(text):
    words = len(sanitize(text).split())
    return words

def averagelen(text):
    words = sanitize(text).split()
    letters = 0
    for word in words:
        letters += len(word)
    
    return letters / len(words)