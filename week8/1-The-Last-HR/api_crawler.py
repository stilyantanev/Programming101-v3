import requests
import json


class Crawler:

    HACKBULGARIA_API = "https://hackbulgaria.com/api/students/"

    def __init__(self):
        self.data = self.download_api(Crawler.HACKBULGARIA_API)

    def get_data(self):
        return self.data

    def download_api(self, url):
        response = requests.get(url).json()

        return response

    def save_to_json_file(self, filename):
        with open(filename, "w") as json_file:
            info = json.dumps(self.data, indent=True, ensure_ascii=False)
            json_file.write(info)

    @staticmethod
    def load_from_json_file(filename):
        with open(filename, "r") as json_file:
            data = json.loads(json_file.read())

        return data
