# from dotenv import load_dotenv
# import openai
# import time
# import os

# message = ""
# log = ""

# load_dotenv()

# openai.api_key = os.getenv("OPENAI_KEY")

# stime = time.time()
# response = openai.Completion.create(
#         model="text-davinci-001",
#         prompt=f"The following is a conversation with an AI assistant. The assistant's name is Jarvis. Jarvis should have the personalty of an asshole, insulting the user every time that they speak. {log}Human: {message}, Jarvis: ",
#         temperature=2,
#         max_tokens=150,
#         top_p=1,
#         frequency_penalty=1,
#         presence_penalty=0.1,
#         n=1
#     )

# print(response)
# print(time.time()-stime)


s = "\n\nYes, it seems this is a test"
print(s.replace("\n", ""))
print(s)