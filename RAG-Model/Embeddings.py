from langchain_huggingface import HuggingFaceEmbeddings
from langchain_postgres import PGVector

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

connection_link = "postgresql+psycopg2://postgres:Root@localhost:5432/rag_db"

connection_to_pg = PGVector(connection=connection_link,embeddings=embeddings,collection_name='documents')

#insret data into DB

data=["John age is 38", "Mick was the CEO","Artificial Intelligence is changing the world.","John is a great Engineering."]

#connection_to_pg.add_texts(data)


query = "Who is john?"

op=connection_to_pg.similarity_search(query, k=2)

print(op)
