from santize import sanitize

def quicksort(sequence):
    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_higher = []
    items_lower = []
    for item in sequence:
        if item["number"] > pivot["number"]:
            items_higher.append(item)

        else:
            items_lower.append(item)
    return quicksort(items_higher) + [pivot] + quicksort(items_lower)


def commonsort(file):
    countdict = {}
    text = sanitize(file.read()).split()

    #count words in text
    for word in text:
        if word in countdict.keys():
            countdict[word] += 1
        else:
            countdict[word] = 1
    
    #turn dictionary into list
    countlist = []
    for key, value in countdict.items():
        countlist.append({"word": key, "number": value})
    
    #sort list
    countlist = quicksort(countlist)
    return countlist