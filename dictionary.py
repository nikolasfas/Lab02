class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str, transl: list):
        if word.isalpha():

            if word not in self.dictionary.keys():
                self.dictionary[word] = []

            for parola in transl:
                if parola.isalpha():
                    self.dictionary[word].append(parola)
                    #print(f"Parola {parola} aggiunta come traduzione a {word}!")
               #else:
                    #print(f"La parola {parola} non può essere aggiunta dato che contiene caratteri non ammessi! ")

    def translate(self, word: str):
        if word.isalpha() and word in self.dictionary.keys():
            translation = self.dictionary[word]
            return translation
        else:
            return  None



    def translateWordWildCard(self):
        pass