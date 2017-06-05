import json  # Gets list of webpages and their type - from opensource.co

path = 'C:\\Users\jasiek\Google Drive\AGH\Semestr IV\Python\zad3\\factcheck\opensource_co.json'
with open(path, encoding='utf-8') as data_file:
    data = json.loads(data_file.read())


# Gets domains from url
def urlparser(url):
    length = len(url)
    if url.startswith("https://"):
        url = url[8:length]
    if url.startswith("http://"):
        url = url[7:length]
    if "/" in url:
        slash = url.index("/")
        if url.startswith("www."):
            url = url[4:slash]
        else:
            url = url[0:slash]
    return url


# Checks if source is classified as 'fake'
def checkfaketype(url):
    if url not in data:
        return -1
    else:
        t1 = data[url]['type']
        t2 = data[url]['2nd type']
        t3 = data[url]['3rd type']
        if ("fake" in t1 or "fake" in t2 or "fake" in t3):
            return 1
        else:
            return 0


# Works best with domain-only url as argument
# webpagecheck("http://www.bbc.com/sport/live/tennis/39832463
def webpagecheck(url):
    url = urlparser(url)
    b = checkfaketype(url)
    if (b == -1):
        print("Source is unknown, however probably reliable.")
        return True
    if (b == 1):
        print("News from this source are probably fake!")
        return False
    if (b == 0):
        print("News from this source are reliable!")
        return True
    return None
