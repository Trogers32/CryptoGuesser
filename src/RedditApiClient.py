from datetime import datetime


class RedditApiClient:
    def __init__(self, requests, settings):
        self.requests = requests
        self.settings = settings
        headers = {'User-Agent': 'CryptoGuesser/0.0.1'}
        self.headers = {**headers, **{'Authorization': f"bearer {self.settings['api_token']}"}}

    def authorize(self):
        auth = self.requests.auth.HTTPBasicAuth(self.settings['auth_token'], self.settings['auth_key'])

        data = {
            'grant_type': 'client_credentials',
            'username': self.settings['username'],
            'password': self.settings['password']
        }

        res = self.requests.post(
            'https://www.reddit.com/api/v1/access_token',
            auth=auth, data=data, headers=self.headers
        )

        self.settings['api_token'] = res.json()['access_token']
        self.headers['Authorization'] = f"bearer {self.settings['api_token']}"

    def get_hot_listing(self):
        returned_posts = []
        res = self.requests.get(
            'https://oauth.reddit.com/r/CryptoCurrency/hot.json',
            headers=self.headers,
            params={'limit': 100}
        )

        for post in res.json()['data']['children']:
            returned_posts.append({
                'title': post['data']['title'],
                'score': post['data']['score'],
                'created_on': datetime.fromtimestamp(post['data']['created_utc'])
            })

        return returned_posts
