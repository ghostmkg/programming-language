# RAG - Retrieval Augmented Generation 
# -------------------------
# WHY RAG?
# -------------------------
# LLMs often hallucinate or provide factually incorrect data.
# They may also fail to answer personal or domain-specific queries.
# RAG (Retrieval-Augmented Generation) solves this by:
# 1. Providing a knowledge base (documents) which is chunked and embedded.
# 2. Retrieving relevant chunks based on a user query.
# 3. Passing both the query and retrieved chunks to the LLM.
# The result is a response that is grounded in factual data and personalized info.
# ---------

# eg of usage : rag pipelines can be implemented in chatbots amd websites to make them better personalised.

# rag pipeline : load doc -> spit into chunks -> embed chunks and store embeddings in vector stores -> retrieve embeddings similar to query -> pass query+retreived docs in llm(invoke)


# following is example code of a rag pipeline , mock_knowlwdge base is robotics club annual magazine

# -------------------------
# IMPORTS & ENV SETUP
# -------------------------
from dotenv import load_dotenv  # To load API keys from .env
load_dotenv()  # Make sure you have your keys set; beginners often forget this

import os  # For file path handling
import pdfplumber  # To read PDFs (our mock knowledge base)
from langchain_groq import ChatGroq  # LLM used for answering queries
from langchain.chains import RetrievalQA  # To integrate vector store with LLM
from langchain_community.vectorstores import Chroma  # Vector store to save embeddings
from langchain_google_genai import GoogleGenerativeAIEmbeddings  # Embeddings generator
from langchain.text_splitter import RecursiveCharacterTextSplitter  # To split long PDFs into chunks

# -------------------------
# 1 >> PDF Loading
# -------------------------
def load_pdf_text(path: str) -> str:
    """
    Extracts all selectable text from a PDF file.
    
    Args:
        path (str): Path to PDF file.
    
    Returns:
        str: Combined text from all pages of the PDF.
    
    Notes:
        - pdfplumber only extracts selectable text.
        - Non-text content (images, scanned PDFs) will be ignored.
    """
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# -------------------------
# 2 >> Text Splitter
# -------------------------
def split_text(text: str, chunk_size: int = 1500, chunk_overlap: int = 50) -> list[str]:
    """
    Splits large text into smaller chunks for better embedding and retrieval.

    Args:
        text (str): Text to split.
        chunk_size (int): Maximum characters per chunk.
        chunk_overlap (int): Number of overlapping characters between chunks to preserve context.

    Returns:
        list[str]: List of text chunks.
    
    Notes:
        - Overlap ensures that information spanning across chunk boundaries is not lost.
        - Smaller chunks improve vector search precision.
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

# -------------------------
# 3 >> Embeddings
# -------------------------
# Initialize embedding model
# This model converts text chunks into vectors so that similarity can be computed.
embedding_model = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
# alternative : you can use hugging face embedding model

# -------------------------
# 4 >> Process Multiple PDFs
# -------------------------
def process_pdfs(folder_path: str) -> list[dict]:
    """Extracts and splits text from all PDFs in a folder and adds source metadata."""
    all_chunks = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            text = load_pdf_text(path)
            chunks = split_text(text)
            # store metadata with each chunk
            chunks_with_source = [{"text": chunk, "source": filename} for chunk in chunks]
            all_chunks.extend(chunks_with_source)
    return all_chunks

# -------------------------
# 5 >> Create or Load Vector Store
# -------------------------
def create_vector_store(chunks_with_source: list[dict], persist_dir: str = "./db") -> Chroma:
    """Creates and persists a Chroma vector store from text chunks."""
    texts = [c["text"] for c in chunks_with_source]
    metadatas = [{"source": c["source"]} for c in chunks_with_source]

    vector_db = Chroma.from_texts(
        texts,
        embedding=embedding_model,
        metadatas=metadatas,
        persist_directory=persist_dir
    )
    return vector_db

def load_vector_store(persist_dir: str = "./db") -> Chroma | None:
    """Load existing Chroma vector store if it exists."""
    if os.path.exists(persist_dir):
        return Chroma(persist_directory=persist_dir, embedding_function=embedding_model)
    return None

# -------------------------
# 6 >> Run full pipeline
# -------------------------
folder_path = r"rag\resources"

# Try loading existing vector store
vector_store = load_vector_store(persist_dir="./db")

# If not present, process PDFs and create vector store
if vector_store is None:
    chunks_with_source = process_pdfs(folder_path)
    vector_store = create_vector_store(chunks_with_source, persist_dir="./db")

# -------------------------
# 7 >> RAG Retrieval + QA
# -------------------------

# Create a retriever from the vector store
retriever = vector_store.as_retriever(
    search_type="mmr", # Maximal Marginal Relevance to reduce redundancy
    search_kwargs={"k": 5, "lambda_mult": 0.5} # Top 5 docs, mix of relevance + diversity
)

# Initialize LLM
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=1.5,  # Controls randomness, creativity
)

# Connect retriever with LLM
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",  # or "map_reduce"
    retriever=retriever,
    return_source_documents=False
)

# Example query
user_query=["Who were members of atomquest team?",
            "what is approach to make agentic chatbot?",
            "What is tech fest of iit bombay?"]

print("Test queries")
for query in user_query:
  result = qa_chain.invoke({"query": query})
  print("------------------------------")
  print("User : "+query)
  print("LLM : "+ result['result'])

