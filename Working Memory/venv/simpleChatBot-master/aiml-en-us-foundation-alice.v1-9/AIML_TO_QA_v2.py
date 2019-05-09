"""
AIML2.0 Tags: Topic -> Catagory -> Pattern -> Template

MAPPINGS:

1 file -> 1 Knowledge Base : dictionary {"Topic":"FilaName", "Chunks":SetsList[Set1(Q,A[]), Set2(Q, A[])...] }
Filename -> Topic
Category -> Set(Q,A) -> Q:String , A: List[Strings]

"""

aiml_file = open("aiml-en-us-foundation-alice/alice.aiml", "r")
qa_file = open("aiml_to_qa/map0_v2.txt", "w")

lines = aiml_file.readlines()

knowledge_base = {} #empty dictionary

# labels for dictionary
topic = "topic"
chunk = "chunk"
#question_pattern = "question_pattern"
#response_list  = "response_list"
topic_name = aiml_file.name.split("/")[1].split(".")[0]
print("topic name : ", topic_name)

knowledge_base[topic] = topic_name

print("knowledge_base : ", knowledge_base)

listOfChunks = []
qa_tuple = ()
qa_dict = {}
question_pattern = ""
response_list = []

import re

category_regex = r"<category>((.|\n)*?)<\/category>"
pattern_regex = r"<pattern>((.|\n)*?)<\/pattern>"
template_regex = r"<template>((.|\n)*?)<\/template>"
template_list_regex = r"<random>((.|\n)*?)<\/random>"

catecory_matches = re.finditer(category_regex, str(lines), re.MULTILINE)
for category_match in catecory_matches:
    # print(match.group(1))
    category = category_match.group(1)
    # print("type : ", type(category))
    pattern_matches = re.finditer(pattern_regex, category, re.MULTILINE)
    template_matches = re.finditer(template_regex, category, re.MULTILINE)
    for pattern_match in pattern_matches:
        pattern = pattern_match.group(1)
        print("pattern : ", pattern)
    for template_match in template_matches:
        template = template_match.group(1)
        print("template : ", template)




# import json
#
# json_kb = json.dumps(knowledge_base, sort_keys=True, indent=4)
#
# print("json kb : ")
# print(json_kb)
#
# with open("aiml_to_qa/json_kb.json", 'w') as json_file:
#     json.dump(knowledge_base, json_file)
#
#
