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
question_pattern = "question_pattern"
response_list  = "response_list"

topic_name = aiml_file.name.split("/")[1].split(".")[0]
print("topic name : ", topic_name)

knowledge_base[topic] = topic_name

print("knowledge_base : ", knowledge_base)

index:str = getStartingLine(lines:str)


counter = 0
for line in lines:
    counter += 1
    if line.startswith("<category>"):
        break
    # print("x : ", x)
    # print("line : ", line)
print("counter : ", counter)

