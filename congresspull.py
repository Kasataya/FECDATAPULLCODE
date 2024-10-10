import requests
import pandas as pd
import os

# Constants
API_KEY = "XhhkejxydJbo8Yz5F94ce0wSlkzeE53kpZJcCJNU"  # Replace with your actual API key
BASE_URL = "https://api.congress.gov/v3/amendment"

def fetch_amendments(api_key, limit=250, offset=0):
    all_data = []
    params = {
        'api_key': api_key,
        'limit': limit,
        'offset': offset,
        'format': 'json'  # You can change this to 'xml' if needed
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'amendments' in data:
            all_data.extend(data['amendments'])
            print(f"Fetched {len(data['amendments'])} records.")
        else:
            print("No 'amendments' found in the response.")
    else:
        print(f"Request error: {response.status_code} {response.reason} - {response.text}")

    return all_data

def save_to_csv(data):
    df = pd.DataFrame(data)
    directory = 'C:/Users/kasse/OneDrive/Desktop/FECDATAPULLCODE/CSV_FILES_OF_FEC_100/'
    
    if not os.path.exists(directory):
        os.makedirs(directory)

    file_path = os.path.join(directory, 'amendments_data.csv')
    df.to_csv(file_path, index=False)
    print(f"Data saved to {file_path}")

def main():
    amendments_data = fetch_amendments(API_KEY)
    if amendments_data:
        save_to_csv(amendments_data)
    else:
        print("No amendments data fetched.")

if __name__ == "__main__":
    main()
