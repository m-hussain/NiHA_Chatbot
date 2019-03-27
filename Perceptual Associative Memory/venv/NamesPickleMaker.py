import pickle

#
# def RawCSVToPickle(SourceFileName, PickleName):
#     source = open(SourceFileName, "r")
#     target = open(PickleName, "wb")
#     # target = open(PickleName, "a")
#     target_text = open("SortedNames.txt", "w")
#     lines = source.readlines()
#     namesList = []
#     for line in lines:
#         list = line.split(",")
#         namesList.append(list[1])
#     print("Names count : ", len(namesList))
#     # print("Names List : ", namesList)
#     print("first element : ", namesList[0], "   last element : ", namesList[-1])
#     namesList.sort()
#     sortedNamesList = namesList
#     print("names count after sorting : ", len(sortedNamesList))
#     # print("sorted names list : ", sortedNamesList)
#     print("first element : ", sortedNamesList[0], "   last element : ", sortedNamesList[-1])
#     print("Dumping in pickle...")
#     pickle.dump(sortedNamesList, target)
#     for name in sortedNamesList:
#         target_text.write(name+"\n")
#
#     print("closing source and pickle files..")
#     source.close()
#     target.close()
#     target_text.close()
#
#
# RawCSVToPickle("NamesSource.txt", "NamesPickle_Sorted")

######################
#
# print("re opening pickle..")
# source = open("NamesPickle_Sorted", "rb")
#
# sortedNamesList = pickle.load(source)
#
# # print("data : ", data)
# print("item count : ", len(sortedNamesList))
#
# print("first element : ", sortedNamesList[0], "   last element : ", sortedNamesList[-1])
#
# source.close()

############################

# import pickle
#
# source = open("MuslimNames.txt", "r")
# source1 = open("SortedNames.txt", "r")
# target = open("SortedAllNames.txt", "w")
#
# lines = source.read()
# lines = lines.split("\n")
#
# lines1 = source1.read()
# lines1 = lines1.split("\n")
#
#
# print(len(lines))
#
# print(len(lines1))
#
# lines.extend(lines1)
#
# print(len(lines))
#
# lines.sort()
#
# print(lines[:5])
# print(lines[-5:-1])
#
# for line in lines:
#     target.write(line+"\n")
#

import pickle

source = open("SortedAllNames.txt", "r")
target = open("AllNamesSortedPickle", "wb")


lines = source.read()
lines = lines.split("\n")

print("Lines : ", lines)

pickle.dump(lines, target)

source.close()
target.close()


#####################

print("re opening pickle..")
source = open("AllNamesSortedPickle", "rb")

sortedNamesList = pickle.load(source)

# print("data : ", data)
print("item count : ", len(sortedNamesList))

print("first element : ", sortedNamesList[0], "   last element : ", sortedNamesList[-1])

source.close()

###########################
