import requests
import re
import sys
import os

# --- Input ---
if len(sys.argv) < 2:
    print("Usage: python3 email-check.py <domain>")
    sys.exit(1)

domain = sys.argv[1]
output_filename = f"unique-{domain}.txt"

url_base = f"https://leaksapi.p.rapidapi.com/api/v2/query/{domain}"
headers = {
    "x-rapidapi-host": "leaksapi.p.rapidapi.com",
    "x-rapidapi-key": "KEY GOES HERE",
    "Accept-Encoding": "identity"
}
params = {
    "type": "domain"
}

def fetch_all_emails():
    offset = 0
    batch_size = 1000
    emails = set()

    while True:
        params["offset"] = offset
        print(f"\n[*] Requesting offset {offset}–{offset + batch_size} for {domain}...")

        try:
            response = requests.get(url_base, headers=headers, params=params)
        except Exception as e:
            print("Request failed:", e)
            break

        if response.status_code != 200:
            print(f"[!] Request failed at offset {offset} with status code {response.status_code}")
            print("Response text:", response.text[:300])
            break

        body = response.text

        # Extract emails
        found_emails = re.findall(r'"email"\s*:\s*"([^"]+)"', body, re.IGNORECASE)
        print(f"[+] Emails found in this batch: {len(found_emails)}")

        if not found_emails:
            print("[!] No more emails found. Stopping.")
            break

        emails.update(email.lower() for email in found_emails)
        offset += batch_size

    return sorted(emails)

# --- Run ---
if __name__ == "__main__":
    all_emails = fetch_all_emails()

    if all_emails:
        with open(output_filename, "w") as f:
            for email in all_emails:
                f.write(email + "\n")

        print(f"\n[✓] Total unique emails found for {domain}: {len(all_emails)}")
        print(f"[✓] Saved to: {output_filename}")
    else:
        print(f"\n[!] No emails found for {domain}.")
