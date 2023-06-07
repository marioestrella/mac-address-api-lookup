# MAC Address API Lookup

## Description
The "MAC Address API Lookup" project is a Python program that queries the MAC address lookup API provided by alldatafeeds.com. It allows users to retrieve information about MAC addresses by providing the MAC address as input. The program sends a request to the API and returns the provided MAC address along with the corresponding OUI (Organizationally Unique Identifier) vendor company name. This tool is designed to assist network administrators, developers, and anyone working with MAC addresses.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation
To use the "MAC Address API Lookup" program as a Docker container, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/mac-address-api-lookup.git`
2. Navigate to the project directory: `cd mac-address-api-lookup`
3. Build the Docker image:
```
docker build -t mac-address-api-lookup
```
4. Run the Docker container
```
docker run --rm -e DATAFEEDS_API_KEY=<api_key_value> mac-address-api-lookup <argument>
```
Replace `<your_api_key>` with your actual API key obtained from alldatafeeds.com, and `<mac_address>` with the MAC address you want to look up. The program will send a request to the MAC address lookup API and display the provided MAC address along with the corresponding OUI vendor company name in the console.

Note: Make sure you have Docker installed on your system before proceeding with the installation.
```
mac_address: AA:BB:CC:DD:EE:FF 
company_name: Vendor XYZ
```

## Contributing
Contributions to the "MAC Address API Lookup" project are welcome. If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. Please adhere to the project's code of conduct when contributing.

## License
This project is licensed under the [MIT License](LICENSE).
