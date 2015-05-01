from histogram import Histogram
import requests
import json


class Crawler:

    @staticmethod
    def get_valid_links(already_parsed_html, webpage):
        all_valid_links = []
        part_of_link = "link.php?id="

        for tag in already_parsed_html.find_all('a'):
            if tag.get('href') is not None:
                if part_of_link in tag.get('href'):
                    all_valid_links.append(webpage + '/' + tag.get('href'))

        return all_valid_links

    @staticmethod
    def get_server_headers(links):
        names_of_servers = []
        our_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36\
            (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36"
        }

        for link in links:
            try:
                response = requests.head(
                    link, timeout=3, allow_redirects=True, headers=our_headers)
                if "Server" in response.headers:
                    names_of_servers.append(response.headers["Server"])
                    print(response.headers["Server"])
            except requests.exceptions.RequestException:
                pass

        return names_of_servers

    @staticmethod
    def group_servers_by_name(server_names):
        frequent_names = ["Apache", "Microsoft-IIS", "nginx", "lighttpd"]
        grouped_servers = Histogram()

        for server_name in server_names:
            for frequent_name in frequent_names:
                if frequent_name in server_name:
                    grouped_servers.add(frequent_name)

        return grouped_servers

    @staticmethod
    def save(filename, names):
        with open(filename, "w") as text_file:
            text_file.write(json.dumps(names, indent=True))

        print("Saving completed successfully!")

    @staticmethod
    def load(filename):
        with open(filename, "r") as text_file:
            # content = text_file.read().split("\n")
            content = text_file.read()
            data = json.loads(content)

        print("Loading completed successfully!")

        return data
