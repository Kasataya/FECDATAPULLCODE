import requests
import pandas as pd
import os
from API_KEYS import api_keys
from API_ENDPOINTS import endpoints

class ApiDataExporter:
    def __init__(self, base_url, endpoint, per_page=100):
        self.base_url = base_url
        self.endpoint = endpoint
        self.url = base_url + endpoint
        self.per_page = per_page
        self.api_keys = api_keys
        self.current_api_key_index = 0

    def fetch_page(self, page):
        params = {'per_page': self.per_page, 'page': page, 'api_key': self.api_keys[self.current_api_key_index]}
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Request error: {e}")
            return None

    def fetch_all_pages(self):
        all_data = []
        page = 1
        while True:
            data = self.fetch_page(page)
            if data and 'results' in data:
                fetched_data = data['results']
                if not fetched_data:
                    break
                all_data.extend(fetched_data)
                print(f"Fetched {len(fetched_data)} records from page {page}. Total records: {len(all_data)}")
                page += 1
                if len(all_data) >= 1000:
                    break
            else:
                print("No data or error in response.")
                break

        return all_data

    def save_to_excel(self, all_data):
        df = pd.DataFrame(all_data)
        file_name = self.format_filename(self.endpoint) + '.xlsx'
        directory = 'C:/Users/kasse/OneDrive/Desktop/FECDATAPULLCODE/EXCEL_FILES_OF_FEC/'
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory '{directory}' created.")

        df.to_excel(file_path, index=False, engine='openpyxl')
        print(f"Data saved to file '{file_path}'.")

    @staticmethod
    def format_filename(endpoint):
        return endpoint.replace('/', '_').replace('?', '_').replace('&', '_')

    def run(self):
        all_data = self.fetch_all_pages()
        if all_data:
            self.save_to_excel(all_data)
        else:
            print(f"No data fetched for endpoint '{self.endpoint}'.")

def main():
    base_url = "https://api.open.fec.gov/v1/"
    for endpoint in endpoints:
        exporter = ApiDataExporter(base_url, endpoint)
        exporter.run()

if __name__ == "__main__":
    main()
