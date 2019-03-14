import nltk
from nltk.tree import Tree

from nltk import ne_chunk_sents, ne_chunk

text = input()

#expanded code
# y = nltk.sent_tokenize(text)
# print(y)
#
# x = []
# for sent in y:
#     z = nltk.word_tokenize(sent)
#     x.append(z)
# print(x)
# tagged_sents = nltk.pos_tag_sents(x)
#
# print(tagged_sents)

tagged_sents = nltk.pos_tag_sents(nltk.word_tokenize(sent) for sent in nltk.sent_tokenize(text))

print(tagged_sents)

ne_tagged_sents = ne_chunk(tagged_sents)

print(ne_tagged_sents)


# # #
# # # sentences = n.sent_tokenize(text)
# # #
# # # print(sentences)
# # # word_tokens = []
# # # for sentence in sentences:
# # #     word_tokens =
# #
# # #sentence = input()
# # # word_tokens = n.word_tokenize(sentence)
# # # print(word_tokens)
# # #
# # # posTags = n.pos_tag(word_tokens)
# #
# sentence = [["there","is","a","cat"],["cat", "is", "on", "mat"]]
# posTag = nltk.pos_tag_sents(sentence)
# print(posTag)
#
# posTag = nltk.pos_tag(["there","is","a","cat"])
# print(posTag)
#
# # pos_sents = n.pos_tag_sents((sentences, lang='eng')
# #
# # print(pos_sents)
