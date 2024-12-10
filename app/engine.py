from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings
from llama_index.llms.gemini import Gemini
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from app.config import Config


class QueryEngine:
    def __init__(self):
        documents = SimpleDirectoryReader(input_files=Config.INPUT_FILES).load_data()

        llm = Gemini(
            api_key=Config.GEMINI_API_KEY,
            model=Config.GEMINI_MODEL,
            temperature=Config.TEMPERATURE,
            top_p=Config.TOP_P,
            top_k=Config.TOP_K,
        )

        embed_model = HuggingFaceEmbedding(model_name=Config.EMBEDDING_MODEL)
        text_splitter = SentenceSplitter(
            chunk_size=Config.CHUNK_SIZE, chunk_overlap=Config.CHUNK_OVERLAP
        )

        Settings.llm = llm
        Settings.embed_model = embed_model
        Settings.text_splitter = text_splitter

        self.index = VectorStoreIndex.from_documents(documents, show_progress=True)
        self.query_engine = self.index.as_query_engine()

    def query(self, prompt: str):
        return self.query_engine.query(prompt)
