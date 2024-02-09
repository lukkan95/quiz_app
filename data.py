import requests

API_PATH = "https://opentdb.com/api.php?amount=10&type=boolean"

question_data = []
response = requests.get(url=API_PATH).json()["results"]
for elem in response:
    question_data.append(elem)

