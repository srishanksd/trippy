from agents.pipeline import Pipeline
from langchain_google_genai import ChatGoogleGenerativeAI 
from agents.weather import WeatherAgent
from agents.maps_agent import MapsAgent
from agents.search_agent import SearchAgent
from agents.content_extractor import ContentExtractorAgent
from agents.pdf_maker import PDFMaker
import random

def main():
    maps = MapsAgent()
    weather = WeatherAgent()
    content = ContentExtractorAgent()
    llm = ChatGoogleGenerativeAI(
        model = "gemini-2.5-flash",
        temperature=0.5
    ) 
    place = input("Enter your place that you want to visit: ")
    budget = input("Budget : " )
    no_persons = input("Enter no of people that they are going: ")
    age = input("Age of the persons: ")
    preferences = input("preferences for your trip: ")
    a = Pipeline(maps, weather, content, llm,place, no_persons, budget,age,preferences)
    report_html = a.report_maker(llm)
    pdf = PDFMaker()
    pdf.create_pdf(report_html, f".//pdfs//trip{random.randint(1,10000)}.pdf")



if __name__ == "__main__":
    main()
    print("Pdf downloaded!!")
