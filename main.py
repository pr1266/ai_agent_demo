import os
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
os.system("cls")

model = OllamaLLM(model="llama3:8b")

template = """
you are an expert in answering questions about a pizza restaurant
here are some relevant reviews : {reviews}
here is a question to answer : {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

while True:
    print("*"*30)
    question = input("ask your question : ")
    if(question == "q"):
        break
    
    result = chain.invoke({
        "reviews": [],
        "question": question
    })

    print(result)
