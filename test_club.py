from main import Person, Club
from unittest import TestCase, main
prs1: Person = Person(123, 20)
prs2: Person = Person(100, 50)
prs3: Person = Person(50, 50)
prs4: Person = Person(200, 51)
persons: list[Person] = [
    prs1, prs2, prs3, prs4
]
class TestClub(TestCase) :
    def setUp(self):
        self.__club = Club()
        for prs in persons:
            self.__club.addPerson(prs)
            
    def test_add_existing_person(self):
        with self.assertRaises(ValueError):
            self.__club.addPerson(prs1)
    def test_add_unexisting_person(self):
        prsNew: Person = Person(1, 100)
        self.__club.addPerson(prsNew)
        self.assertEqual(prsNew, self.__club._Club__sortedSet[0])
        self.assertEqual(prsNew, self.__club._Club__sortedKeyList[-1])
        
    def test_getAllSortedId(self) :
        self.assertListEqual([prs3, prs2, prs1, prs4], self.__club.getAllSortedId())  
        
    def test_getAllSortedAgeId(self) :
        self.assertListEqual([prs1, prs3, prs2, prs4], self.__club.getAllSortedAgeId()) 
        
    def test_getPersonsByAge(self)  :
        self.assertListEqual([prs3, prs2], self.__club.getPersonsByAge(25, 50)) 
                   
if __name__ == "__main__" :
    main()       
        