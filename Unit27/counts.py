def repetition(elements):
    counts = [elements.count(i) for i in elements]
    return elements[counts.index(max(counts))] if elements else None