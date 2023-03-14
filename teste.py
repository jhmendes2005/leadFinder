import requests
from bs4 import BeautifulSoup

class GoogleMapsScraper:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    def search_places(self, location, radius, keywords):
        results = []
        base_url = 'https://www.google.com/maps/search/'
        
        for keyword in keywords:
            print(f'Buscando por "{keyword}"...')
            url = f'{base_url}{keyword}/@{location},{radius}m/data=!3m1!1e3'
            print(url)
            try:
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                print(f"Error in search_places for {keyword}: {e}")
                continue
            
            soup = BeautifulSoup(response.content, 'html.parser')
            places = soup.select('.section-result')
            print(response.content)
            
            for place in places:
                name = place.select_one('.section-result-title span').text
                address = place.select_one('.section-result-location span').text
                try:
                    phone = place.select_one('.section-result-phone-number').text
                except AttributeError:
                    phone = ''
                try:
                    website = place.select_one('.section-result-action-icon-button[data-tooltip="Abrir o site"]').get('href')
                except AttributeError:
                    website = ''
                
                results.append({
                    'name': name,
                    'address': address,
                    'phone': phone,
                    'website': website,
                    'keyword': keyword
                })

                print(results)
        
        return results
    

scrap = GoogleMapsScraper()

scrap.search_places("-23.550520,-46.633308", 50000, ['restaurante'])
