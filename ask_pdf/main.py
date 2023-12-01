

import argparse

from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma


def main(pdf: str, query: str) -> str:
    """_summary_

    Args:
        pdf (str): _description_
        query (str): _description_

    Returns:
        str: _description_
    """
    loader = UnstructuredPDFLoader(pdf)
    pages = loader.load_and_split()
    embeddings = OpenAIEmbeddings()
    docsearch = Chroma.from_documents(pages, embeddings).as_retriever()
    docs = docsearch.get_relevant_documents(query)
    chain = load_qa_chain(ChatOpenAI(temperature=0), chain_type="stuff")
    return chain.run(input_documents=docs, question=query)

def main_cli() -> str:
    parser = argparse.ArgumentParser(description="Answer questions from a PDF")
    parser.add_argument("-f", "--file", type=str, help="The PDF file to read", default="Final Report on Guidelines on default definition (EBA-GL-2016-07).pdf")
    parser.add_argument("-q", "--query", type=str, help="The question to answer")
    args = parser.parse_args()
    return main(args.file, args.query)