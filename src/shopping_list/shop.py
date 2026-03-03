import sys
import os
import json
from storage import load_list, save_list

def add_item(shopping_list):
    """
    Pievieno jaunu produktu produktu sarakstam.
    """
    item = input("Ievadi preci: ")
    price_input = input("Ievadi preces cenu: ")
    try:
        price = float(price_input)
        shopping_list.append({"name": item, "price": price})
        print(f"✓ Pievienots: {item} ({price:.2f} EUR)")
        return True
    except ValueError:
        print("Kļūda: Cena nav derīgs skaitlis! Mēģiniet vēlreiz.")
        return False

def list_item():
    """
    Parāda esošo iepirkumu sarakstu
    """
    shopping_list = load_list()
    if not shopping_list:
        print("Iepirkumu saraksts ir tukšs!")
        return
    print("Iepirkumu saraksts:")
    for i, l in enumerate(shopping_list, 1):
        print(f"{i}. {l['item']} - {l['price']}")

def total_price():
    """
    Aprēķina kopējo iepirkumu summu.
    """
    shopping_list = load_list()
    summa = 0.0
    item_count = len(shopping_list)
    for shop in shopping_list:
        summa += shopping_list['price']
    print(f"Kopējā summa: {summa:.2f} EUR ({item_count} produkti)")


def clear_list():
    """
    Nodzēš iepirkumu sarakstu un saglabā tukšu sarakstu.
    """
    empty_list = []
    storage.save_list(empty_list)
    print("✓ Iepirkumu saraksts ir notīrīts!")

if __name__ == "__main__":
    shopping_list = load_list()
    add_item(shopping_list)
    list_item()
    total_price(shopping_list)
    clear_list()
