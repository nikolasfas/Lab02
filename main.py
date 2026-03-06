import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")


while(True):

    print("---------------------------------")
    print("     Translator Alien-Italian    ")
    print("---------------------------------")

    t.printMenu()

    txtIn = input()

    # Add input control here!

    if int(txtIn) >= 1 and int(txtIn) <= 5:

        if int(txtIn) == 1:
            print("Okay, quale parola devo aggiungere?")
            txtIn = input()
            t.handleAdd(txtIn)
            continue
        if int(txtIn) == 2:
            print("Okay, quale parola devo cercare?")
            txtIn = input()
            t.handleTranslate(txtIn)
            continue
        if int(txtIn) == 3:
            print("Okay, quale parola devo cercare?")
            txtIn = input()
            t.handleWildCard(txtIn)
            continue
        if int(txtIn) == 4:
            print("Okay, stampo tutto il dizionario!")
            for elem in t.dictionary.dictionary.items():
                print(elem[0], " ", elem[1])
            continue
        if int(txtIn) == 5:
            print("Chiudo il programma! Ciau!")
            break