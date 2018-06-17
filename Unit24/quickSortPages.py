def quickSortPages(pages, ranks):
    if not pages or len(pages) <=1: 
        return pages
    else:
        pivot, worse, better = ranks[pages[0]], [], []
        for page in pages[1:]:
            if ranks[page] <= pivot:
                worse.append(page)
            else:
                better.append(page)
        return quickSortPages(better, ranks) + [pages[0]] + quickSortPages(worse, ranks)