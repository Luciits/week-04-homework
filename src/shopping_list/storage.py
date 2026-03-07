import json
import os

SHOPPING_FILE = "shopping.json"
PRICES_FILE = "prices.json"

def load_list():
    """
    Ielādē iepirkumu sarakstu.

    """
    if not os.path.exists(SHOPPING_FILE):
        return []
    with open(SHOPPING_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_list(items):
    """
    Saglabā iepirkumu sarakstu.

    """
    with open(SHOPPING_FILE, "w", encoding="utf-8") as f:
        json.dump(items, f, indent=2, ensure_ascii=False)

def load_prices():
    """
    Ielādē cenu sarakstu.

    """
    if not os.path.exists(PRICES_FILE):
        return {}
    with open(PRICES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_prices(prices):
    """
    saglabā cenu sarakstu

    """
    with open(PRICES_FILE, "w", encoding="utf-8") as f:
        json.dump(prices, f, indent=2, ensure_ascii=False)

def get_price(name):
    
    prices = load_prices()
    return prices.get(name)

def set_price(name, price):
    prices = load_prices()
    prices[name] = round(float(price), 2)
    save_prices(prices)