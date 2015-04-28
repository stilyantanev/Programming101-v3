import requests


class Crawler:

    @staticmethod
    def get_valid_links(already_parsed_html, webpage, link):
        all_valid_links = []

        for tag in already_parsed_html.find_all('a'):
            if tag.get('href') is not None:
                if link in tag.get('href'):
                    all_valid_links.append(webpage + tag.get('href'))

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
                if "server" in response.headers:
                    names_of_servers.append(response.headers["Server"])
                    print(response.headers["Server"])
            except requests.exceptions.RequestException:
                pass

        return names_of_servers

    @staticmethod
    def save_server_names_in_file(names, filename):
        with open(filename, "w") as text_file:
            text_file.write("\n".join(names))

        print("Saving completed successfully!")

    @staticmethod
    def load_server_names_from_file(filename):
        with open(filename, "r") as text_file:
            content = text_file.read().split("\n")

        print("Loading completed successfully")

        return content
