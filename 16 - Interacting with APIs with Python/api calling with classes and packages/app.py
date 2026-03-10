import time
from libs.openexchange import OpenExchangeClient

APP_ID = "f8905fe8f2fe4d1490971a0152fe5845"

client = OpenExchangeClient(APP_ID)

start = time.time()
convert = client.convert(1, "USD", "INR")
print(f"1 USD is equal to {convert} INR")
end = time.time()
print(end - start)

start = time.time()
convert = client.convert(1, "USD", "INR")
print(f"1 USD is equal to {convert} INR")
end = time.time()
print(end - start)

start = time.time()
convert = client.convert(1, "USD", "INR")
print(f"1 USD is equal to {convert} INR")
end = time.time()
print(end - start)

eur_to_inr_rate = client.convert(1, "EUR", "INR")
print(f"1 EUR is equal to {eur_to_inr_rate} INR")

convert = client.convert(1, "KYD", "INR")
print(f"1 KYD is equal to {convert} INR")

convert = client.convert(1, "CHF", "INR")
print(f"1 CHF is equal to {convert} INR")

gbp_to_inr_rate = client.convert(1, "GBP", "INR")
print(f"1 GBP is equal to {gbp_to_inr_rate} INR")

convert = client.convert(1, "GIP", "INR")
print(f"1 GIP is equal to {convert} INR")

convert = client.convert(1, "JOD", "INR")
print(f"1 JOD is equal to {convert} INR")

convert = client.convert(1, "OMR", "INR")
print(f"1 OMR is equal to {convert} INR")

convert = client.convert(1, "BHD", "INR")
print(f"1 BHD is equal to {convert} INR")

convert = client.convert(1, "KWD", "INR")
print(f"1 KWD is equal to {convert} INR")

usd_to_gbp_rate = client.convert(1000, "USD", "GBP")
print(f"1000 USD is equal to {usd_to_gbp_rate} GBP")

gbp_to_usd_rate = client.convert(1000, "GBP", "USD")
print(f"1000 GBP is equal to {gbp_to_usd_rate} USD")

kwd_to_inr_rate = client.convert(1000, "KWD", "INR")
print(f"1000 KWD is equal to {kwd_to_inr_rate} INR")
