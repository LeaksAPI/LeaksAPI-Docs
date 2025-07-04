import http.client
import json
import sys

# Check that a domain was provided
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <domain>")
    sys.exit(1)

# Get the domain from command-line arguments
domain = sys.argv[1]

# Set up HTTPS connection
conn = http.client.HTTPSConnection("leaksapi.p.rapidapi.com")

# Set request headers with your API key and host
headers = {
    'x-rapidapi-key': "YOUR KEY HERE",
    'x-rapidapi-host': "leaksapi.p.rapidapi.com"
}

# Make the GET request to the API for the specified domain
endpoint = f"/api/v2/query/{domain}?type=domain"
conn.request("GET", endpoint, headers=headers)

# Get and read the response
res = conn.getresponse()
data = res.read()

# Decode the response data and parse as JSON
parsed_json = json.loads(data.decode("utf-8"))

# Pretty print the parsed JSON with indentation
print(json.dumps(parsed_json, indent=2))
