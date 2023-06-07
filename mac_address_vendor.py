import requests
import argparse
import os

api_key = os.environ.get('DATAFEEDS_API_KEY')
if api_key is not None:
    print(f"API Key has been Provided")
else:
    print('Missing API Key')

parser = argparse.ArgumentParser(description='MAC Address Company Lookup')
parser.add_argument('mac_address', help='MAC address to look up')
args = parser.parse_args()


def mac_lookup_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("GET request failed.")
        print("Status code:", response.status_code)


json = mac_lookup_request(
    "https://mac-address.alldatafeeds.com/api/v1?apiKey=" + api_key + "&output=json&search=" + args.mac_address)
print('mac_address: ' + args.mac_address + '\ncompany_name: ' + json['vendorDetails']['companyName'])
