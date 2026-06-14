import os
import chromadb
from chromadb.utils import embedding_functions

import os
import chromadb
from chromadb.config import Settings  # <-- Add this import
from chromadb.utils import embedding_functions

class CampusVectorStore:
    def __init__(self):
        # Establish the absolute storage path matching our global project architecture
        self.persist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/vector_db"))
        os.makedirs(self.persist_dir, exist_ok=True)

        # SILENCE TELEMETRY: Disable anonymous usage logging to clean up terminal streams
        self.chroma_client = chromadb.PersistentClient(
            path=self.persist_dir,
            settings=Settings(anonymized_telemetry=False)  # <-- Add this setting
        )
        
        # Configure local default embedding utility function (384-dimensional space)
        self.embedding_fn = embedding_functions.DefaultEmbeddingFunction()
        
        # Connect to or safely initialize our unified campus knowledge base collection
        self.collection = self.chroma_client.get_or_create_collection(
            name="campus_knowledge",
            embedding_function=self.embedding_fn
        )
    
    # ... leave the rest of the index_processed_chunks and search_similar_chunks methods exactly as they are!
    def index_processed_chunks(self, chunks: list[dict]) -> bool:
        """
        Takes overlapping text paragraph structures, extracts string contents, 
        maps individual unique IDs, and saves them straight into ChromaDB storage vectors.
        """
        if not chunks:
            print("[VECTOR DB] Warning: Received empty chunk array for indexing.")
            return False

        documents = []
        metadatas = []
        ids = []

        for idx, chunk in enumerate(chunks):
            documents.append(chunk["text"])
            metadatas.append(chunk["metadata"])
            ids.append(f"chk_{chunk['metadata']['source']}_{chunk['metadata']['page']}_{idx}")

        try:
            self.collection.upsert(
                documents=documents,
                metadatas=metadatas,
                ids=ids
            )
            print(f"[VECTOR DB] Successfully upserted {len(documents)} context fragments into ChromaDB storage.")
            return True
        except Exception as e:
            print(f"[VECTOR DB ERROR] Bulk document upsert failure: {str(e)}")
            return False

    def search_similar_chunks(self, query_text: str, n_results: int = 3) -> list[dict]:
        """
        Queries ChromaDB using vector similarity to retrieve the top-k most 
        relevant context paragraph fragments with metadata tracking coordinates.
        """
        try:
            results = self.collection.query(
                query_texts=[query_text],
                n_results=n_results
            )
            
            formatted_chunks = []
            if not results or not results["documents"] or not results["documents"][0]:
                return formatted_chunks
                
            # ChromaDB returns nested batch lists; extract the first query's data
            matched_documents = results["documents"][0]
            matched_metadatas = results["metadatas"][0]
            
            for i in range(len(matched_documents)):
                formatted_chunks.append({
                    "text": matched_documents[i],
                    "source": matched_metadatas[i].get("source", "Unknown Document"),
                    "page": matched_metadatas[i].get("page", 0)
                })
                
            print(f"[VECTOR DB SEARCH] Located {len(formatted_chunks)} relevant matches matching query text.")
            return formatted_chunks
            
        except Exception as e:
            print(f"[VECTOR DB QUERY CRASH] Similarity search failed: {str(e)}")
            return []