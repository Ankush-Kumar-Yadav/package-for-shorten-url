import requests

class BitlyShortener:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api-ssl.bitly.com/v4/shorten'

    def shorten_url(self, long_url, custom_alias=None, use_random_alias=False):
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json',
        }

        payload = {
            'long_url': long_url,
            'domain': 'bit.ly',
        }

        if custom_alias:
            payload['custom_bitlink'] = custom_alias
        elif use_random_alias:
            payload['title'] = 'Random Alias'

        response = requests.post(self.base_url, headers=headers, json=payload)

        if response.status_code == 200:
            return response.json()['id']
        else:
            response.raise_for_status()

# Example Usage:
# shortener = BitlyShortener(api_key='YOUR_BITLY_API_KEY')
# short_url = shortener.shorten_url('https://www.example.com')
# print(f'Short URL: {short_url}')
