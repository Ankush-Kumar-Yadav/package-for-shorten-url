# package-for-shorten-url
The `shortenurlpy` library provides a simple Python interface to shorten long URLs using the Bitly API. It is designed to make URL shortening easy and straightforward for developers who want to integrate this functionality into their projects.
# shortenurlpy

## Overview
The `shortenurlpy` library provides a simple Python interface to shorten long URLs using the Bitly API. It is designed to make URL shortening easy and straightforward for developers who want to integrate this functionality into their projects.

## Installation
Ensure you have Python installed on your system.

1. Install the library using pip:
   ```bash
   pip install shortenurlpy
from shortenurlpy import BitlyShortener

# Replace 'YOUR_BITLY_API_KEY' with your actual Bitly API key
shortener = BitlyShortener(api_key='YOUR_BITLY_API_KEY')

# Shorten a long URL
long_url = 'https://www.example.com'
short_url = shortener.shorten_url(long_url)
print(f'Short URL: {short_url}')
