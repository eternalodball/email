import requests

url = "https://mailcheck.p.rapidapi.com/"
print()
YOUR_DOMAIN = input('[+] ' 'Enter your email or domain to check: ')
print()
YOUR_API = "9b1b4e72d6mshe601fb8d92e915ap14ba13jsnbf615ace9699"
#YOUR_API = input('[+] ' 'Enter your API KEY: ')
print()
print('[+] Checking if domain sould be blocked')

querystring = {"domain": YOUR_DOMAIN}

headers = {
    'x-rapidapi-host': "mailcheck.p.rapidapi.com",
    'x-rapidapi-key': YOUR_API
    }

response = requests.request("GET", url, headers=headers, params=querystring)

temp = response.json()

print()
print(temp)
print()
