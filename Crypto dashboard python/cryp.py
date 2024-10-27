import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime


API_URL = "https://api.coingecko.com/api/v3/simple/price"
CURRENCY = "bitcoin"
CURRENCY_PAIR = "usd"
INTERVAL = 5  


times = []
prices = []


def fetch_price():
    try:
        response = requests.get(API_URL, params={"ids": CURRENCY, "vs_currencies": CURRENCY_PAIR})
        response.raise_for_status()
        price = response.json()[CURRENCY][CURRENCY_PAIR]
        return price
    except (requests.RequestException, KeyError) as e:
        print("Error fetching price:", e)
        return None


def update(i):
    price = fetch_price()
    if price:
        current_time = datetime.now().strftime("%H:%M:%S")
        times.append(current_time)
        prices.append(price)
        if len(times) > 10:
            times.pop(0)
            prices.pop(0)
        
        ax.clear()
        ax.plot(times, prices, marker='o', color='b')
        ax.set_title(f"Live {CURRENCY.capitalize()} Price in {CURRENCY_PAIR.upper()}")
        ax.set_xlabel("Time")
        ax.set_ylabel(f"Price ({CURRENCY_PAIR.upper()})")
        plt.xticks(rotation=45)
        plt.tight_layout()

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, interval=INTERVAL * 1000)  

plt.show()