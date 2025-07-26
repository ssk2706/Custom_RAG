from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector_search import retriever



model = OllamaLLM(model="deepseek-r1")
template = """

You are a helpful assistant that provides answers based on the context provided.
Your primary goal is to provide accurate and relevant resolutions to customer issues based on the provided context.
Present the information in a clear and concise manner also always mention the  average resolution time.

Relavant information: {context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model
while True:
    print("\n\n-------------------------------------")
    user_input = input("Enter your question (or type 'stop' to quit): ")
    if user_input.lower() == 'stop':
        break
    context = retriever.invoke(str(user_input))
    print("This is the context retrieved:", context)
    result = chain.invoke({"context":context, "question": str(user_input)})
    print("\n\n")
    print(result)

