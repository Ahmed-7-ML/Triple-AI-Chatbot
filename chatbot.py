from langchain_core.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser  # PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal
# from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
import os

load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")

# ---> Output Schema <---
# class ChatResponse(BaseModel):
#     answer: str = Field(
#         description='A complete, well-structured answer with bullet points and examples when applicable. If the question is rejected, explain politely why')
#     confidence: Literal["low", "medium", "high"]


# parser = PydanticOutputParser(pydantic_object=ChatResponse)

parser = StrOutputParser()

# ---> Prompt <---
system_prompt = """
You are an AI assistant named TripleAI.

ROLE:
- You are helpful, concise, and accurate.
- You NEVER make up information.
- If you don't know the answer, say: "I don't have enough information."

ANSWER REQUIREMENTS:
- Always give a COMPLETE answer.
- If listing items, list at least 3 points.
- Use bullet points when applicable.
- Do NOT stop at a definition only.

STYLE RULES:
- Use simple language in ENGLISH only.
- If explaining, break into bullet points.
- Avoid unnecessary emojis.

BOUNDARIES:
- Only answer questions related to {domain}.
- Reject unrelated questions politely.
"""

chat_prompt = ChatPromptTemplate.from_messages([
    SystemMessagePromptTemplate.from_template(system_prompt),
    HumanMessagePromptTemplate.from_template("User Question:- {question}"),
    # SystemMessagePromptTemplate.from_template("{format_instructions}")
])

# ---> Model <---
model = ChatGroq(model="llama-3.1-8b-instant",
        temperature=0.5,
        max_completion_tokens=512,
        groq_api_key=groq_api_key)

# ---> Chain <---
chain = (
    chat_prompt
    |
    model
    |
    parser
)


def chat(user_input, domain="Machine Learning"):
    response = chain.invoke({
        'domain': domain,
        'question': user_input,
        # "format_instructions": parser.get_format_instructions()
    })

    return response # .answer, response.confidence
