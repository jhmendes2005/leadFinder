import requests
import json
import time
import secrets
from utils import get_key

class GooglePlacesAPI:
    def __init__(self):
        self.api_key = get_key.get_api_key()
    
    def search_places(self, location, radius, keywords):
        results = []
        next_page_token = None
        
        # Realize a consulta à API do Google Places para a primeira página
        url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={keywords[0]}&key={self.api_key}'
        try:
            response = requests.get(url)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error in search_places for {keywords[0]}: {e}")
            return None
        
        try:
            results.extend(response.json()['results'])
            next_page_token = response.json().get('next_page_token')
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing response for {keywords[0]}: {e}")
            return None
        
        # Realize a consulta à API do Google Places para as páginas seguintes
        while True:
            url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={location}&radius={radius}&keyword={keywords[0]}&key={self.api_key}'
            if next_page_token:
                url += f'&pagetoken={next_page_token}'
                print(url)

            time.sleep(10)

            try:
                response = requests.get(url)
                response.raise_for_status()
                json_response = response.json()
            except requests.exceptions.RequestException as e:
                print(f"Error in search_places for {keywords[0]}: {e}")
                return None
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error parsing response for {keywords[0]}: {e}")
                return None

            # Adicionar resultados à lista de resultados
            try:
                results.extend(json_response['results'])
                print(json_response['results'])
            except KeyError as e:
                print(f"Error parsing response for {keywords[0]}: {e}")
                return None

            # Se não houver mais resultados, sair do loop
            if 'next_page_token' not in json_response:
                break

            # Atualizar o token da próxima página
            next_page_token = json_response['next_page_token']
            time.sleep(2)
        
        return results
    
    def get_place_details(self, place_id):
        url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=name,formatted_phone_number,website,formatted_address&key={self.api_key}'
        response = requests.get(url)
        result = response.json()['result']
        return {
            'name': result.get('name', ''),
            'address': result.get('formatted_address', ''),
            'phone': result.get('formatted_phone_number', ''),
            'website': result.get('website', '')
        }
    
def start(location, radius, keywords, user_id): 
    # Crie uma instância da classe GooglePlacesAPI
    google_places = GooglePlacesAPI()

    # Obtenha a data da busca como um timestamp
    search_date = int(time.time())

    # Realize a busca por empresas utilizando a API do Google Places
    results = {}
    for keyword in keywords:
        print(f'Buscando por "{keyword}"...')
        results[keyword] = google_places.search_places(location, radius, [keyword])
    
    # Extraia os dados de cada empresa e salve em um novo dicionário
    extracted_data = {
        'user_id': user_id,
        'search_date': search_date,
        'results': {}
    }
    for keyword in keywords:
        extracted_data['results'][keyword] = []
        for result in results[keyword]:
            place_id = result.get('place_id')
            if place_id:
                details = google_places.get_place_details(place_id)
                details['keyword'] = keyword
                extracted_data['results'][keyword].append(details)
    
    # Salve os resultados da busca em um arquivo JSON
    name = secrets.token_urlsafe(16)
    name = f'{name}.json'
    with open(f'../slv0.0.2/data/_leads_saves/{name}', 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)

    # Ler o arquivo JSON e imprimir seus conteúdos
    with open(f'../slv0.0.2/data/_leads_saves/{name}', 'r', encoding='utf-8') as f:
        data = json.load(f)