import os
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
os.system("cls")

model = OllamaLLM(model="llama3:8b")

template = """
you are an expert in answering questions about a pizza restaurant
here are some relevant reviews : {reviews}
here is a question to answer : {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

result = chain.invoke({
    "reviews": [],
    "question": "what is the best pizza of this restaurant?"
})

print(result)