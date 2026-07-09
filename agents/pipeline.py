from .weather import WeatherAgent
from .maps_agent import MapsAgent
from .search_agent import SearchAgent
from .content_extractor import ContentExtractorAgent
from datetime import date, timedelta
import os
from dotenv import load_dotenv

load_dotenv()


# tomorrow = today + timedelta(days=1)

weather = WeatherAgent()
map_agent = MapsAgent()
search_agent = SearchAgent()
content = ContentExtractorAgent()



class Pipeline:
    def __init__(self,maps, weather, content, llm,  place, no_persons, budget,age, preferences):
        self.maps = maps
        self.weather = weather
        self.content = content
        self.llm = llm
        self.place = place
        self.no_persons = no_persons
        self.budget = budget
        self.age = age
        self.preferences = preferences
        self.date = str(date.today())
        
    def _get_location(self):
        x = self.maps.search(self.place)
        return self.maps.extract_data(x)
    
    def _get_wether(self):
        latitude = self._get_location()['latitude']
        longitude = self._get_location()['longitude']
        x = self.weather.search(latitude, longitude)
        return self.weather.extract_data(x, self.date)
    
    def collect_information(self):
        return self.content.data_extract(f"Find the gems hidden and some tourist places near {self.place}!")
        
        
    def clean_data(self):
        unclean_data = self.collect_information()
        prompt = f"""
        You are a travel planner.
        Extract only useful travel information therse are some preferences should be considered {self.preferences}  with the age of people {self.age}.
        Return JSON.
        Destination:
        {self.place}
        Data:
        {unclean_data}
        Required JSON:
        {{
            "hidden_gems": [],
            "restaurants": [],
            "tips": [],
            "warnings": []
        }}
        """
        return self.llm.invoke(prompt).content 
    
    def report_maker(self, llm):
        wea = self._get_wether()
        weather_data = f"Max_temp = {wea['max_temp']}, Min_temp = {wea['min_temp']}, weather = {wea['weather']}"
        clean_data = self.clean_data()
        prompt = prompt = f"""
        You are an expert travel planner.
        Destination: {self.place}
        People: {self.no_persons}
        Budget: {self.budget}
        Preferences: {self.preferences}
        Weather:
        {weather_data}
        Travel Information:
        {clean_data}
        Instructions:
        - Use the supplied weather as the highest priority.
        - Use the supplied travel information as the primary source.
        - Use your own knowledge only to improve the itinerary without contradicting the supplied information.
        - Recommend the best travel date based on the weather and explain why.
        - Optimize the itinerary by grouping nearby attractions.
        - Keep recommendations within the user's budget.
        Generate a COMPLETE HTML document.
        Requirements:
        - Include internal CSS inside a <style> tag.
        - Make the page modern, colorful and professional.
        - Use cards with rounded corners and subtle shadows.
        - Use a clean font.
        - Use different colors for headings and important sections.
        - Make tables attractive.
        - Use emojis where appropriate.
        - Make the page A4 printable.
        - Use responsive spacing and good typography.
        Include the following sections:
        - Trip Summary
        - Best Travel Date
        - Day-wise Itinerary
        - Hidden Gems
        - Restaurants & Local Food
        - Packing Checklist
        - Travel Tips
        - Important Warnings
        - Estimated Budget
        - dont make pdf look like empty make it filled or written something and not mention budget and preferences on top
        Return ONLY valid HTML after i am converting it to the pdf so make it nicely according to it.
        Do not use Markdown.
        Do not wrap the HTML inside code fences.
        Do not include any explanation.
        """
        return llm.invoke(prompt).content
    
        