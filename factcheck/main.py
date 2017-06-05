from factcheck.opensrc import webpagecheck
from factcheck.wolfram import checkfact


def main():
    webpagecheck("www.aszdziennik.pl/news12345")
    checkfact("What is the meaning of life?", "42")
    return None


main()
