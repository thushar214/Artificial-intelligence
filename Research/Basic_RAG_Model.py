import psycopg2
from sentence_transformers import SentenceTransformer

from Research.Embeddings import embeddings

#Data
data = ["Mick is lawyer","John is software engineer","Cena was a werslter"]


def DB_conn():

    DB_Config = {
         "host" : "localhost",
         "port": 5432,
         "database": "rag_db",
         "user": "postgres",
         "password":"Root"
    }

    DB_Init = psycopg2.connect(**DB_Config)
    cursor = DB_Init.cursor()

    cursor.execute("""
     Select * from langchain_pg_embedding
    """)


def New_embeddings(data):

    model = SentenceTransformer("all-MiniLM-L6-v2")
    embeddings = model.encode(data)
    vector_store = []

    for doc, emb in zip(data,embeddings):
        vector_store.append({"text" : doc , "embeddings" : embeddings})

    return vector_store
