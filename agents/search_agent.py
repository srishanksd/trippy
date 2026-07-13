from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("TAVILY_API_KEY")


class SearchAgent:
    def __init__(self):
        self.client = TavilyClient(api_key=api_key)
    
    def search(self, query):
        response = self.client.search(
            query=query,
            max_results=7,
            include_images=False
        )
        return response
    
    def extract_data(self, data):
        results = []

        for result in data["results"]:
            if result["score"] > 0.70:
                results.append({
                    "title": result["title"],
                    "url": result["url"],
                    "snippet": result["content"]
                })
                
        return results
    