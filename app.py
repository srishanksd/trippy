from flask import Flask, render_template, request
from agents.pipeline import Pipeline
from langchain_google_genai import ChatGoogleGenerativeAI 
from agents.weather import WeatherAgent
from agents.maps_agent import MapsAgent
from agents.search_agent import SearchAgent
from agents.content_extractor import ContentExtractorAgent
from agents.pdf_maker import PDFMaker
import random
from flask import send_file

maps = MapsAgent()
weather = WeatherAgent()
content = ContentExtractorAgent()
llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    temperature=0.5
)



app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':
        budget = int(request.form['budget'])
        preferences = request.form['preferences']
        age = int(request.form['age'])
        persons = int(request.form['persons'])
        place = request.form['place']
        a = Pipeline(maps, weather, content, llm,place, persons, budget,age,preferences)
        report_html = a.report_maker(llm)
        import os
        os.makedirs("pdfs", exist_ok=True)
        pdf_maker = PDFMaker()
        pdf_maker.create_pdf(report_html, f".//pdfs//trip{random.randint(1,10000)}.pdf")
        
        
        filename = f".//pdfs//trip{random.randint(1,10000)}.pdf"

        pdf_maker.create_pdf(report_html, filename)

        return send_file(
            filename,
            as_attachment=True
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)