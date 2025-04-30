# retrieval.py

def retrieve_documents(query):
    
    documents = [
        "The Earth revolves around the Sun.",
        "Water boils at 100 degrees Celsius.",
        "The Declaration of Independence was signed in 1776.",
        "Python is a programming language created by Guido van Rossum.",
        "The capital of France is Paris."
    ]

    results = [doc for doc in documents if query.lower() in doc.lower()]
    return results
