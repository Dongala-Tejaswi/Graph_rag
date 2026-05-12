def generate_answer(query, context):

    prompt = f"""
    You are an AI assistant.

    Context:
    {context}

    User Question:
    {query}

    Give a detailed answer.
    """

    answer = f"""
    Based on retrieved context:

    {context}

    Answer:
    Graph RAG combines graph traversal
    and vector retrieval for better AI reasoning.
    """

    return answer