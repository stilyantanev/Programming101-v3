from histogram import Histogram
from crawler import Crawler
from chart import Chart
from bs4 import BeautifulSoup
import requests


def main():

    # Get parsed_html of given website
    webpage = "http://register.start.bg"
    response = requests.get(webpage)
    parsed_html = BeautifulSoup(response.text)

    # Get server name of websites in parsed html and save it to json file
    links_to_pages = Crawler.get_valid_links(parsed_html, webpage)
    servers = Crawler.get_server_headers(links_to_pages)
    Crawler.save("servers.json", servers)

    # Group server names by most common types and save it to json file
    grouped_servers_histogram = Crawler.group_servers_by_name(servers)
    grouped_servers = grouped_servers_histogram.dictionary
    Crawler.save("servers_by_groups.json", grouped_servers)

    # Load most common server names from json file
    server_histogram = Histogram()
    server_histogram.dictionary = Crawler.load("servers_by_groups.json")

    # Get keys and valus from frquent_servers_histogram and make plot
    keys = list(server_histogram.dictionary.keys())
    values = list(server_histogram.dictionary.values())
    Chart.make_plot(keys, values)

if __name__ == '__main__':
    main()
