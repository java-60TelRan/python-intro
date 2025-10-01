from main import Dictionary
from unittest import TestCase, main
words = [
            "Application", "Apple", "aPproach", "aPPreciate", "apricot", "above", "about"
]
class TestDictionary(TestCase):
    def setUp(self):
        self.__dictionary = Dictionary()
        for word in words: self.__dictionary.addWord(word)
        
    def test_add_existing_word (self):
        with self.assertRaises(ValueError) :
            self.__dictionary.addWord(words[0]) 
        with self.assertRaises(ValueError) :
            self.__dictionary.addWord("aPpLiCaTiOn")      
            
    def test_add_non_existing_word(self):
        self.__dictionary.addWord("a")
        self.assertEqual("a", self.__dictionary._Dictionary__words_sorted[0])
        self.__dictionary.addWord("big")
        self.assertEqual("big", self.__dictionary._Dictionary__words_sorted[-1])
        
    def test_get_words_by_existing_prefix(self):
        self.assertListEqual(sorted(words, key=str.casefold), self.__dictionary.getWordsByPrefix("a"))
        self.assertListEqual(sorted(words[0:4], key=str.casefold), self.__dictionary.getWordsByPrefix("APP"))
        self.assertListEqual(sorted(words[0:5], key=str.casefold), self.__dictionary.getWordsByPrefix("Ap"))
       
    def test_get_words_by_non_existing_prefix(self):  
        self.assertListEqual([], self.__dictionary.getWordsByPrefix("bA"))
        
if __name__ == "__main__":
    main()        
        
           