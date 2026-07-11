from langchain_google_genai import ChatGoogleGenerativeAI 
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature=0.5
)
response = llm.invoke("You are the travel agent for making plan for trip and tell me some best places near tha shorapur in karnataka for 2 days!")
print(response.content)
