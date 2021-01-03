from abc import ABC,abstractmethod

class TouchScreenLaptop(ABC):


    @abstractmethod
    def scroll(self):
        pass

    def click(self):
        pass

class HP(TouchScreenLaptop):
    def scroll(self):
        print("HP scroll")

class Dell(TouchScreenLaptop):
    def scroll(self):
        print("Dell scroll")

class  HPNoteBook(HP):
    def click(self):
        print("HP Notebook click")

class DellNoteBook(Dell):
    def scroll(self):
        print("Dell Notebook click")


hpnotebook=HPNoteBook()
dellnotebook=DellNoteBook()

hpnotebook.click()
hpnotebook.scroll()
dellnotebook.click()
dellnotebook.scroll()
