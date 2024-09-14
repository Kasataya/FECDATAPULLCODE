import requests
import pandas as pd
import os
import time
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

    def get_current_api_key(self):
        return self.api_keys[self.current_api_key_index]

    def rotate_api_key(self):
        # Move to the next API key
        self.current_api_key_index += 1
        # If we've exhausted all keys, wrap around
        if self.current_api_key_index >= len(self.api_keys):
            print("All API keys exhausted. Exiting.")
            return False
        print(f"Switching to API key {self.current_api_key_index + 1}.")
        return True

    def fetch_page(self, page):
        params = {'per_page': self.per_page, 'page': page, 'api_key': self.get_current_api_key()}
        try:
            response = requests.get(self.url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            if response.status_code == 429:
                print(f"API key {self.current_api_key_index + 1} hit rate limit (429).")
                if self.rotate_api_key():
                    time.sleep(2)  # Optional: add a short delay to avoid immediate failure with the new key
                    return self.fetch_page(page)
                else:
                    print("Rate limit hit, and no more API keys available.")
            else:
                print(f"HTTP error occurred: {http_err}")
        except requests.RequestException as req_err:
            print(f"Request error: {req_err}")
        return None

    def fetch_all_pages(self):
        all_data = []
        page = 1
        while True:
            data = self.fetch_page(page)
            if data and 'results' in data:
                fetched_data = data['results']
                if not fetched_data:
                    break  # No more data on this page, stop fetching
                all_data.extend(fetched_data)
                print(f"Fetched {len(fetched_data)} records from page {page}. Total records: {len(all_data)}")
                page += 1
            else:
                print("No data or error in response.")
                break

        return all_data

    def save_to_csv(self, all_data):
        df = pd.DataFrame(all_data)
        file_name = self.format_filename(self.endpoint) + '.csv'
        directory = 'C:/Users/kasse/OneDrive/Desktop/FECDATAPULLCODE/CSV_FILES_OF_FEC/'
        file_path = os.path.join(directory, file_name)

        if not os.path.exists(directory):
            os.makedirs(directory)
            print(f"Directory '{directory}' created.")

        df.to_csv(file_path, index=False)
        print(f"Data saved to file '{file_path}'.")

    @staticmethod
    def format_filename(endpoint):
        return endpoint.replace('/', '_').replace('?', '_').replace('&', '_')

    def run(self):
        all_data = self.fetch_all_pages()
        if all_data:
            self.save_to_csv(all_data)
        else:
            print(f"No data fetched for endpoint '{self.endpoint}'.")

def main():
    base_url = "https://api.open.fec.gov/v1/"
    for endpoint in endpoints:
        exporter = ApiDataExporter(base_url, endpoint)
        exporter.run()

if __name__ == "__main__":
    main()
