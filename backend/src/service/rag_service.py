from src.config.llm import AgentConfig
from langchain_huggingface import ChatHuggingFace

agent_config = AgentConfig()

model = ChatHuggingFace(llm=agent_config.llm)
def mychat(message: str, retriever) -> str:
    # Step 1: Perform the semantic search
    docs = retriever.invoke(message)

    context = "\n\n".join([doc.page_content for doc in docs])

   

    # Step 2: Build prompt
    messages = [
        ("system", "You are a helpful AI assistant. Answer ONLY from the provided context. If not found, say 'I don't know'."),
        ("human", f"""
        Context:
        {context}

        Question:
        {message}
        """)
    ]

    # Step 3: LLM call
    response = model.invoke(messages)

    return response.content