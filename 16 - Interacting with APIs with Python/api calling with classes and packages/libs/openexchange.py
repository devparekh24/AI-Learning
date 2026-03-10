import requests

# import functools
from cachetools import cached, TTLCache


class OpenExchangeClient:
    BASE_URL = "https://openexchangerates.org/api"

    def __init__(self, app_id):
        self.app_id = app_id

    @property
    # @functools.lru_cache(maxsize=2)
    @cached(cache=TTLCache(maxsize=2, ttl=600))  # 600sec = 10 minutes
    def latet(self):
        return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

    def convert(self, from_amt, from_curr, to_curr):
        rates = self.latet["rates"]
        to_rate = rates[to_curr]

        if from_curr == "USD":
            return from_amt * to_rate
        else:
            from_rate = rates[from_curr]
            return (from_amt / from_rate) * to_rate
