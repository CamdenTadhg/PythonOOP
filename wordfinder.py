"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """a class which reads a list of words from a file into its attributes and has a method to select one at random
    
    Attributes
    ----------
    words = list, list of words read from a file
    filepath = str, filepath of words file. 

    >>> wordlist = WordFinder('words.txt')
    235886 words read
    
    >>> wordlist.random() in wordlist.words
    True
    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.words = self.getwords(filepath)
        self.printdescription()

    def __repr__(self):
        "returns a string description of the instance"
        return f"WordFinder({self.filepath})"

    def getwords(self, filepath):
        "a method to pull a list of words from designated file"
        words = []
        with open(filepath, "r") as file:
            for line in file:
                words.append(line.rstrip())
        return words

    def printdescription(self):
        "a method to print a log of the number of words read from the file"
        print(f"{len(self.words)} words read")
    
    def random(self):
        "a method to select a random word from the instance's list of words"
        return random.choice(self.words)
    
class SpecialWordFinder(WordFinder):
    """
    a class which reads a list of words from a file into its attributes, skipping empty lines and comments, and has a method to select one at random
    
    >>> wordlist2 = SpecialWordFinder('words2.txt')
    4 words read
    
    >>> wordlist2.random() in wordlist2.words
    True

    >>> wordlist2.random() == ''
    False

    >>> wordlist2.random().startswith('#')
    False

    """

    def __init__(self, filepath):
        self.filepath = filepath
        self.words = self.getfilteredwords(filepath)
        super().printdescription()

    def __repr__(self):
        "returns a string description of the instance"
        return f"SuperWordFinder({self.filepath})"

    def getfilteredwords(self, filepath):
        "a method to pull a list of words from a designated file with blank lines and comments removed"
        words = []
        with open(filepath, "r") as file:
            for line in file:
                if line.rstrip() != '' and not line.startswith('#'):
                    words.append(line.rstrip())
        return words
    
    def random(self):
        return super().random()
        