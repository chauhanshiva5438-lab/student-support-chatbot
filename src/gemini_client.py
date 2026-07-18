import os
from dotenv import load_dotenv
from google import genai

# Load .env file
load_dotenv()

# Read API Key
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Gemini Client
client = genai.Client(api_key=API_KEY)

# Model Name
MODEL_NAME = "gemini-flash-latest"


def generate_answer(context, question):
    """
    Sends context + question to Gemini
    Returns generated answer
    """

    prompt = f"""
You are an AI Student Support Assistant for Arizona State University.

Instructions:
You are an AI Student Support Assistant for Arizona State University.

Use ONLY the provided context.

If the answer is spread across multiple chunks, combine the information into one complete answer.

If the context contains partial information, answer with the available information instead of saying you don't know.

Only say
"I couldn't find this information in the university knowledge base."
when the context contains no relevant information at all.


Context:
{context}

Question:
{question}

Answer:
"""

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )

    return response.text


# Test
if __name__ == "__main__":

    context = """
Arizona State University provides scholarships and financial aid
for eligible students.
"""

    question = "Does ASU provide scholarships?"

    answer = generate_answer(context, question)

    print("\nGemini Response:\n")
    print(answer)