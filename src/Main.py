import os
import requests
from DataManipulator import determine_relevancy, write_to_file
from RedditApiClient import RedditApiClient


class Main:
    def __init__(self):
        self.settings = os.environ
        self.api_client = RedditApiClient(requests, self.settings)

    def start_guessing(self):
        self.api_client.authorize()
        response_data = self.api_client.get_hot_listing()
        relevant_crypto_coins = determine_relevancy(response_data)
        write_to_file(relevant_crypto_coins)


if __name__ == '__main__':
    Main().start_guessing()
