import http.client

conn = http.client.HTTPSConnection("leaksapi.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "YOUR KEY GOES HERE",
    'x-rapidapi-host': "leaksapi.p.rapidapi.com"
}

conn.request("GET", "/api/v2/query/pizza.co.uk?type=domain", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
