from histogram import Histogram
from crawler import Crawler
from chart import Chart
from bs4 import BeautifulSoup
from pprint import pprint
import requests


def main():

    # Get parsed_html of given website
    webpage = "http://register.start.bg/"
    response = requests.get(webpage)
    parsed_html = BeautifulSoup(response.text)

    # Get header server of every website in parsed html
    link = "link.php?id="
    links_to_pages = Crawler.get_valid_links(parsed_html, webpage, link)
    servers = Crawler.get_server_headers(links_to_pages)

    # Save and load server names in file
    Crawler.save_server_names_in_file(servers, "file.txt")
    server_names = Crawler.load_server_names_from_file("file.txt")

    # Put full server names into histogram
    all_servers_histogram = Histogram()
    for server_name in server_names:
        all_servers_histogram.add(server_name)
    pprint(all_servers_histogram.get_dictionary())

    # Put frequent server names into histogram
    frequent_server_names = ["Apache", "Microsoft-IIS", "nginx", "lighttpd"]
    frequent_servers_histogram = Histogram()
    for server_name in server_names:
        for frequent_server_name in frequent_server_names:
            if frequent_server_name in server_name:
                frequent_servers_histogram.add(frequent_server_name)
    pprint(frequent_servers_histogram.get_dictionary())

    # Get keys and valus from frquent_servers_histogram and make plot
    keys = list(frequent_servers_histogram.dictionary.keys())
    values = list(frequent_servers_histogram.dictionary.values())
    Chart.make_plot(keys, values)

if __name__ == '__main__':
    main()
