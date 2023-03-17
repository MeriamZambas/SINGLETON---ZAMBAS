class WordDisplay:
    __instance = None
    
    def __init__(self):
        if WordDisplay.__instance != None:
            raise Exception("You cannot create more than one instance of WordDisplay.")
        else:
            WordDisplay.__instance = self
    
    def display(self, word):
        print(word)
    
    @staticmethod
    def getInstance():
        if WordDisplay.__instance == None:
            WordDisplay()
        return WordDisplay.__instance
    
wd = WordDisplay.getInstance()
wd.display("Hello") 
wd.display("World") 