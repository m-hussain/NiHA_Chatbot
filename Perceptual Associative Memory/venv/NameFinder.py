import pickle

source = open("AllNamesSortedPickle", "rb")

sortedNamesList = pickle.load(source)


def isName(word:str):
    if word in sortedNamesList:
        return True
    else:
        return False


source.close()


if __name__ == '__main__':
    while True:
        word = input("word : ")

        name = isName(word)

        if name:
            print(word," is a person name..")
        else:
            print(word," is not a person name...")

