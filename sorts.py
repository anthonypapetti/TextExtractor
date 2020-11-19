from santize import sanfile

def quicksort(array, l, r):
    #sorts the array and returns a pivot value
    def partition(array, l, r):
        pivot = array[r]["number"]
        i = l
        for j in range(l, r):
            if i = j:
                continue
            if array[j]["number"] < pivot:
                array[i], array[j] = array[j], array[i]
                i += 1
            array[i + 1], array[r] = array[r], array[i + 1]
            return i + 1
    
    #exit condition
    if l < r:
        pivot = partition(a, l, r)
        quicksort(a, l, pivot - 1)
        quicksort(a, pivot + 1, r)
    return

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
    for key, value in countdict:
        countlist.append({"word": key, "number": value})
    
    #sort list
    quicksort(countlist, 0, len(countlist))
    return countlist