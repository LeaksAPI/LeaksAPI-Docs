
# LeaksAPI-Docs
http://leaks-api.com docs

emails-full-unique.py - increment results using offset until no more are found, unique and save to file (uses around 5-10 credits per full deep domain search)  
add your key 'your key here' in the script 

```
% python3 emails-full.py example.com
[*] Requesting offset 0–1000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 1000–2000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 2000–3000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 3000–4000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 4000–5000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 5000–6000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 6000–7000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 7000–8000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 8000–9000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 9000–10000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 10000–11000 for example.com...
[+] Emails found in this batch: 1000

[*] Requesting offset 11000–12000 for example.com...
[+] Emails found in this batch: 0
[!] No more emails found. Stopping.

[✓] Total unique emails found for example.com: 5466
[✓] Saved to: unique-example.com.txt
```


endpoints;

passwords-premium-subscription

Returns: Passwords, IPs, phone numbers, address, DOB, SSN, and more
Method: GET
URI: /api/v2/query/{email}
Example:
```
curl --request GET \
  --url 'https://leaksapi.p.rapidapi.com/api/v2/query/test@gmail.com' \
  --header 'x-rapidapi-host: leaksapi.p.rapidapi.com' \
  --header 'x-rapidapi-key: YOUR_API_KEY'
```


domain-search
Returns: Leaked data for entire corporate domain
Method: GET
URI: /api/v2/query/{domain}
parameter = type=domain
if none provided, it will auto attempt to auto identify but you should specify domain its better

Example curl request and response:
```
curl --request GET \
  --url 'https://leaksapi.p.rapidapi.com/api/v2/query/example.com?type=domain' \
  --header 'x-rapidapi-host: leaksapi.p.rapidapi.com' \
  --header 'x-rapidapi-key: x'
```

```
< HTTP/2 200 
< date: Fri, 27 Jun 2025 03:10:06 GMT
< content-type: application/json
< x-ratelimit-commercial-full-domain-search-remaining: 939995
< x-ratelimit-commercial-full-domain-search-reset: 17960
< server: RapidAPI-1.2.8
< x-rapidapi-version: 1.2.8
< x-rapidapi-region: AWS - eu-west-1
< 
{
  "found": 1000,
  "result": [
    {
      "email": "somebody@example.com",
      "fields": [
        "password",
        "email"
      ],
      "password": "1$RHLJ57vRhgI",
      "source": {
        "name": "Unknown"
      }
    },
    {
      "first_name": "samynl",
      "fields": [
        "password",
        "first_name",
        "username",
        "email"
      ],
      "source": {
        "compilation": 0,
        "passwordless": 0,
        "breach_date": "2013-11",
        "name": "xSplit",
        "unverified": 0
      },
      "password": "123456",
      "username": "samynl",
      "email": "somebody@example.com"
    },
```
  

