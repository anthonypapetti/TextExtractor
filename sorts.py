from santize import sanfile

def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item["number"] > pivot["number"]:
            items_greater.append(item)

        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)


def commonsort(file):
    countdict = {}
    text = sanfile(file).split()

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
    print(countlist)
    quick_sort(countlist)
    return countlist