import requests

class WHOApiService:
    def __init__(self, api_url):
        self.api_url = api_url

    def get_outbreak_news(self):
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data from WHO API: {e}")
            return None
