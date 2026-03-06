from dictionary import Dictionary


class Translator:

    def __init__(self):
        self.dictionary = Dictionary()

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print(f"1. Aggiungi nuova parola"+"\n"+"2. Cerca una traduzione"+"\n"+"3. Cerca con wildcard"+"\n"+"4. Stampa tutto il dizionario"+"\n"+"5. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        with open(dict, 'r', encoding='utf-8') as f:
            for line in f:
                fields = line.strip().split()
                parola_aliena = fields[0]
                parola_ita = fields[1:]
                self.dictionary.addWord(parola_aliena, parola_ita)


    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        parole = entry.strip().split()
        alieno = parole[0]
        italiano = parole[1:]

        traduzioni = self.dictionary.addWord(alieno, italiano)
        print(f"{traduzioni}" + "\n" + "Aggiunta!")

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        if query.isalpha() and query in self.dictionary.dictionary.keys():
            #translation = self.dictionary.translate(query)
            print(f"{self.dictionary.translate(query)}")
        else:
            print(f"La parola fornita ({query}) non è nel dizionario oppure ha un formato scorretto")

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        traduzioni, parola = self.dictionary.translateWordWildCard(query)
        print(f"{parola}"+"\n"+f"{traduzioni}")

