from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings

def get_embedding_function():
    embeddings = HuggingFaceInferenceAPIEmbeddings(
        api_key="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", model_name="sentence-transformers/all-MiniLM-l6-v2"
    )
    return embeddings
