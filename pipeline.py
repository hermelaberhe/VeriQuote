# pipeline.py

from retrieval import retrieve_documents
from bloom_filter import setup_bloom_filter

def main():
    bloom = setup_bloom_filter()
    query = input("Enter your query: ")

    documents = retrieve_documents(query)
    
    if documents:
        generated_output = documents[0]  
    else:
        generated_output = "The Sun is a cube."  
    
    print(f"\nGenerated Output: {generated_output}")
    
    if generated_output in bloom:
        print("Result: ✅ Verified Quote!")
    else:
        print("Result: ❌ Potential Hallucination Detected!")

if __name__ == "__main__":
    main()
