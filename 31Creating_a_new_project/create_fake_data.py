# I would like to connect to my Ollama server. 
# I want to use the 'phi4:latest' model, I would like to send a prompt to it it asking for fake data, and have it return in a CSV format. 

import requests
import json
import csv
from io import StringIO

class OllamaFakeDataGenerator:
    """
    A class to generate fake data using Ollama's phi4 model
    """
    def __init__(self, base_url="http://localhost:11434"):
        self.base_url = base_url
        self.model = "phi3:mini"
        
    def generate_fake_data(self, num_records=5):
        """
        Generate fake data using the phi4 model.
        """
        payload = {
            "model": self.model,
            "prompt": f"Generate {num_records} fake data records in CSV format."
        }
        try:
            print(f"Sending request to {self.base_url}/api/generate with payload: {payload}")
            response = requests.post(f"{self.base_url}/api/generate", json=payload, timeout=30)
            print("Received response from Ollama server.")
            response.raise_for_status()
            return response.text
        except requests.exceptions.Timeout:
            print("Request to Ollama server timed out.")
        except requests.exceptions.RequestException as e:
            print(f"Error connecting to Ollama server: {e}")
        return None

def save_to_csv(data, filename="fake_data.csv"):
    """
    Save the generated data to a CSV file
    """
    try:
        # Create a file-like object from the string
        csv_file = StringIO(data)
        
        # Read CSV data
        reader = csv.reader(csv_file)
        
        # Write to actual CSV file
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            for row in reader:
                writer.writerow(row)
                
        print(f"Data successfully saved to {filename}")
        
    except Exception as e:
        print(f"Error saving CSV file: {e}")

def main():
    """
    Main function to generate and save fake dataapp
    """
    print("Connecting to Ollama server...")
    
    # Create generator instance
    generator = OllamaFakeDataGenerator()
    
    # Generate fake data
    csv_data = generator.generate_fake_data(num_records=5)
    
    if csv_data:
        # Save to CSV file
        save_to_csv(csv_data)
        print("Data generation complete!")
    else:
        print("Failed to generate fake data.")

if __name__ == "__main__":
    main()