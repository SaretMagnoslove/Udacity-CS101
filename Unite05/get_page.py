def get_page(url):
    try:
        import urllib
        return urllib.request.urlopen(url).read()
    except:
        return
