import aiml
import glob

files = glob.glob("rosie-master/lib/aiml/*.aiml")



# Create the kernel and learn AIML files
kernel = aiml.Kernel()

kernel.learn("basic_chat.aiml")

for file in files:
    print(file)
    kernel.learn(file)

    # kernel.respond(file)
#
# # Press CTRL-C to break this loop
while True:
    print(kernel.respond(input("Enter your message >> ")))


