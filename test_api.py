import requests
import json

def fetch_data_from_server(url, output_filename):
    # Make a GET request to the API endpoint
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        # Extract the JSON string from the response text
        response_text = response.text
        print(response_text)
        json_text = response_text.split('(', 1)[1].rstrip(');')
        
        # Parse the JSON string into a JSON object
        json_data = json.loads(json_text)

        with open(output_filename, 'w') as f:
            json.dump(json_data, f)
        
        print("Data updated in ", output_filename)
    else:
        print("Error occurred while fetching data from API.")

todays_team_url = 'https://fantasy.iplt20.com/daily/services/feed/players?lang=en&gamedayId=9&announcedVersion=04032023184908'
team1_vs_team2_filename = 'file.json'

fetch_data_from_server(todays_team_url, team1_vs_team2_filename)
