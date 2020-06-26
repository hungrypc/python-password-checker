import requests
import hashlib


def request_api_data(query_char):
    # this api takes only the first 5 chars of a hash
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check api and try again')
    return res


def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8'))
    hashed = sha1password.hexdigest().upper()

    first5_chars, tail = hashed[:5], hashed[5:]
    response = request_api_data(first5_chars)
    return response
    # check password if exists in API response



