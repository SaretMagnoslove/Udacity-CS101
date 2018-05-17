from no_links import get_next_target

def print_all_links(page):
    while True:
        url, endpos = get_next_target(page)
        if url:
            print (url)
            page = page [endpos:]
        else:
            break
