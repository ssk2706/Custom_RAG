from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import json
import pandas as pd

df = pd.read_csv(r"tech_support_dataset.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./ChromaDB22"

to_add_docs = not os.path.exists(db_location)
docs_data = []
ids = []

if to_add_docs:
    
    for i, row in df.iterrows():
        documment = Document(
            page_content=row["Customer_Issue"] + " " + 
            row["Tech_Response"] + " Time Taken to Resolve: " 
            + row["Resolution_Time"] + " Category of issue is:" 
            + row["Issue_Category"],
            metadata={
                "Conversation_ID": row["Conversation_ID"],
                "Issue_Status": row["Issue_Status"],
                "resolution_time": row["Resolution_Time"]
            }
        )
        docs_data.append(documment)
        ids.append(str(i))
vector_store = Chroma(
    collection_name= "tech_support",
    persist_directory=db_location,
    embedding_function=embeddings,
)

if to_add_docs:
    vector_store.add_documents(
        documents=docs_data,
        ids=ids
    )
    # vector_store.persist()

retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs= {"k": 5}
    )