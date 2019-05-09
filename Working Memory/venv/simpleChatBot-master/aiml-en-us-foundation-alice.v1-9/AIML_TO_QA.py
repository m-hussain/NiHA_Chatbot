"""
AIML2.0 Tags: Topic -> Catagory -> Pattern -> Template

MAPPINGS:

1 file -> 1 Knowledge Base : dictionary {"Topic":"FilaName", "Chunks":SetsList[Set1(Q,A[]), Set2(Q, A[])...] }
Filename -> Topic
Category -> Set(Q,A) -> Q:String , A: List[Strings]

"""

aiml_file = open("aiml-en-us-foundation-alice/mp0.aiml", "r")
qa_file = open("aiml_to_qa/map0.txt", "w")

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

def getStartingLine(lines):
    counter = 0
    for line in lines:
        if line.startswith("<category>"):
            break
        counter += 1
        # print("x : ", x)
        # print("line : ", line)
    return counter

index = getStartingLine(lines)
print("starting line index : ", index)

aiml = lines[index:]

print(aiml)

listOfSets = []
qa_tuple = ()

qa_dict = {}

import re

#line = aiml[0]
chunk_list = []
response_list = []
response = ""
question_pattern = ""
count = 0
for line in aiml:
    if line.find("<category>") is not -1:
        result = re.search('<category><pattern>(.*)</pattern>', line)
        question_pattern = result.group(1)
        # print(question_pattern)
        qa_dict["pattern"] = question_pattern
    elif line.find("<template>") is not -1:
        result = re.search('<template>(.*)</template>', line)
        response = result.group(1)
        qa_dict["response"] = response
    elif line.find("</category>") is not -1:
        count += 1
        knowledge_base[chunk+str(count)] = qa_dict
        qa_file.write("question_pattern : "+question_pattern+"\n")
        qa_file.write("response : " + response + "\n")
        qa_dict = {}


# print("knowledge base :", knowledge_base[topic])



import json

json_kb = json.dumps(knowledge_base, sort_keys=True, indent=4)

print("json kb : ")
print(json_kb)

with open("aiml_to_qa/json_kb.json", 'w') as json_file:
    json.dump(knowledge_base, json_file)


