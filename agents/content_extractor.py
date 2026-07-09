import trafilatura
from .search_agent import SearchAgent


url_agent = SearchAgent()

class ContentExtractorAgent:
    def __init__(self):
        pass
    
    def data_extract(self,query):
        data = url_agent.search(query)
        results = url_agent.extract_data(data)
        urls = []
        for result in results:
            urls.append(result['url'])
        downloaded = [trafilatura.fetch_url(url) for url in urls]
        articles = [trafilatura.extract(download) for download in downloaded]
        articles = [article for article in articles if article is not None]
        
        return articles




