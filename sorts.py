from sanitize import sanitize

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


def commonsort(intext):
    countdict = {}
    text = sanitize(intext).split()

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

def alphasort(intext):
    def sort(words):
        buckets = {}
        #sort items into buckets
        for word in words:
            if word[0] in buckets.keys():
                buckets[word[0]].append(word)
            else:
                buckets[word[0]] = [word]
        
        #sort buckets
        for bucket in buckets.values():
            for item in bucket:
                #compare to previous elements in list
                for previous_item in bucket[0:bucket.index(item)]:
                    #compare the two items
                    #create copies with stripped apostrophes (na items)
                    item_na = item.replace('\'', '')
                    previous_item_na = previous_item.replace('\'', '')

                    #loop through characters with smallest length iterations
                    if len(item_na) <= len(previous_item_na):
                        loop_len = len(item_na)
                        item_bigger = False
                    else:
                        loop_len = len(previous_item_na)
                        item_bigger = True

                    for i in range(loop_len):
                        #compare characters
                        if ord(item_na[i]) < ord(previous_item_na[i]):
                            #swap
                            bucket[bucket.index(item)], bucket[bucket.index(previous_item)] = bucket[bucket.index(previous_item)], bucket[bucket.index(item)]
                            length_compare = False
                            break
                        if ord(item_na[i]) > ord(previous_item_na[i]):
                            #don't swap
                            length_compare = False
                            break
                        if ord(item_na[i]) == ord(previous_item_na[i]):
                            length_compare = True
                            continue
                    #check if items need to be swapped
                    #based on length
                    if length_compare:
                        if not item_bigger:
                            bucket[bucket.index(item)], bucket[bucket.index(previous_item)] = bucket[bucket.index(previous_item)], bucket[bucket.index(item)]
        return buckets

    text = sanitize(intext).split()
    text = list(set(text))
    text = sort(text)
    alphabet = list(map(chr, range(97, 123)))
    textlist = []
    for letter in alphabet:
        for key in text.keys():
            if key == letter:
                textlist += text[letter]
    return textlist