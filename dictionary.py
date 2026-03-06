class Dictionary:
    def __init__(self):
        self.dictionary = {}

    def addWord(self, word: str, transl: list):
        traduzioni = []
        if word.isalpha():
            traduzioni.append(word)

            if word not in self.dictionary.keys():
                self.dictionary[word] = []

            for parola in transl:
                if parola.isalpha():
                    self.dictionary[word].append(parola)
                    traduzioni.append(parola)
                    print(f"Parola {parola} aggiunta come traduzione a {word}!")
                else:
                    print(f"La parola {parola} non può essere aggiunta dato che contiene caratteri non ammessi! ")
        return traduzioni

    def translate(self, word: str):
        if word.isalpha() and word in self.dictionary.keys():
            translation = self.dictionary[word]
            return translation
        else:
            return  None



    def translateWordWildCard(self, word: str):

        for parola in self.dictionary.keys():

            if len(parola) == len(word):
                match = True
                for i in range(len(word)):
                    if word[i] != "?" and word[i] != parola[i]:
                        match = False
                        continue

                if match:
                    word = parola
                    return self.dictionary[word], parola


