import requests
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAI API")
parser.add_argument("file_name", help="The name of the file that you want to create" )
args = parser.parse_args()

MODEL = "text-davinci-003"


api_endpoint = "https://api.openai.com/v1/completions"
api_key = os.getenv("OPENAI_API_KEY")

headers = {
    "Content-Type" : "application/json",
    "Authorization" : "Bearer " + api_key
}

request_data = {
    "model" : MODEL,
    "prompt": f"Provide a python script to {args.prompt}. Provide code only, no text",
    "max_tokens": 500,
    "temperature": 0.5

}


r = requests.post(url=api_endpoint, headers=headers, json=request_data)
data = r.json()


if r.status_code == 200:
    response = data["choices"][0]["text"]
    with open(f"{args.file_name}", "w") as file:
        file.write(response)
else:
    print("Request failed")
