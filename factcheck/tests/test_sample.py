# Sample Test passing with nose and pytest
from factcheck.wolfram import checkfact
from factcheck.opensrc import urlparser
from factcheck.opensrc import webpagecheck


class TestClass(object):

    def test_life(self):
        assert checkfact("What is the meaning of life", "42") == True

    def test_firetruck(self):
        assert checkfact("Why are firetrucks red?", "Because they can") == False

    def test_urlparser(self):
        assert urlparser("http://bbc.co.uk/news1234") == "bbc.co.uk"

    def test_urlparser2(self):
        assert urlparser("http://www.bbc.co.uk/news1234") == "bbc.co.uk"

    def test_webpage(self):
        assert webpagecheck("gazeta.pl/news123") == True

    def test_webpage2(self):
        assert webpagecheck("www.aszdziennik.pl/news12345") == False
