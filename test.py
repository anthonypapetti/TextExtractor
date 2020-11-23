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

    return quicksort(items_lower) + [pivot] + quicksort(items_higher)

print(quicksort([{"word": "e", "number": 5}, {"word": "e", "number": 6}, {"word": "e", "number": 7}, {"word": "e", "number": 8}, {"word": "e", "number": 9}, {"word": "e", "number": 8}, {"word": "e", "number": 7}, {"word": "e", "number": 1}, {"word": "e", "number": 3}, {"word": "e", "number": 21}, {"word": "e", "number":56}, {"word": "e", "number": 5}, {"word": "e", "number": 6}, {"word": "e", "number":90}, {"word": "e", "number": 4}, {"word": "e", "number": 7}, {"word": "e", "number": 8}, {"word": "e", "number": 9}, {"word": "e", "number": 0}]))