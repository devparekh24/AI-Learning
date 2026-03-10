import requests

API_KEY = "f8905fe8f2fe4d1490971a0152fe5845"
ENDPOINT = "https://openexchangerates.org/api/latest.json"


def usd_to_gbp_rate():
    url = f"{ENDPOINT}?app_id={API_KEY}"
    response = requests.get(url)
    data = response.json()["rates"]
    usd_amt = 1000
    gbp_amt = usd_amt * data["GBP"]
    print(f"{usd_amt} USD is equal to {gbp_amt} GBP")
    # print("data", data)
    # return data


usd_to_gbp_rate()
