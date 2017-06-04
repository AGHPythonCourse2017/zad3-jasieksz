from factcheck.factcheck.opensrc import webpagecheck
from factcheck.factcheck.wolfram import checkfact


def main():
    webpagecheck("gazeta.pl")
    checkfact("What is the meaning of life?","42")
    return None

main()
