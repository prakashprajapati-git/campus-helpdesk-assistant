import sys
import os

# Adjust paths so execution handles internal app imports cleanly
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from app.rag.rag_pipeline import RAGPipeline

def run_diagnostic():
    print("============ INITIATING LIVE RAG SEARCH DIAGNOSTIC ============")
    
    # Try searching for a concept likely inside your uploaded admission file
    test_query = "admission requirements or criteria"
    print(f"Testing Live Vector Query Lookup for: '{test_query}'...\n")
    
    search_result = RAGPipeline.query_knowledge_base(test_query)
    
    print("--- AI SYNTHESIZED ANSWER STREAM ---")
    print(search_result["answer"] + "\n")
    
    print("--- VERIFIED PAGE SOURCE CITATIONS ---")
    print(search_result["sources"])
    print("\n================================================================")

if __name__ == "__main__":
    run_diagnostic()