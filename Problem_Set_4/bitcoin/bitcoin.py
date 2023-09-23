import sys
import requests

if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = float(o["bpi"]["USD"]["rate"].replace(",", ""))
    amount = rate * float(sys.argv[1])
    print(f"${amount:,.4f}")
except requests.RequestException:
    pass
