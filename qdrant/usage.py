from langchain.document_loaders import CSVLoader

import qdrant
# Initialize the Qdrant instance
# Replace 'url' and 'api_key' with your Qdrant host and API key.
qdrant_client = qdrant.Qdrant(collection_name="aipg")

loader = CSVLoader(file_path="../document_parsing/aipg/aipg.csv", encoding='utf-8-sig')

docs = loader.load()
print(docs[5].page_content)

# Add documents to the Qdrant collection
qdrant_client.add_vectors(docs)

# Perform a search
search_query = "Who is jojo"
search_results = qdrant_client.search_vectors(search_query)

# Display search results
print("Search Results:")
for result in search_results:
    print(result)
