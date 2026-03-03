# 04 nedēļas mājasdarba sākums
import json
import sys
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """
    Nolasa kontaktus no JSON faila. Ja fails neeksistē, atgriež [].
    """
    if not os.path.exists(CONTACTS_FILE):
        return [] # Atgriež tukšu sarakstu, ja fails vēl nav izveidots
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)
 
def save_contacts(contacts):
    """
    Saglabā kontaktu sarakstu JSON failā.
    """
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        # indent=2 padara JSON failu cilvēkiem lasāmu
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def add_contacts(kontaktu_saraksts):
    """
    Pievieno jaunu kontaktu kontaktu sarakstam
    """
    name = input("Ievadiet kontakta vārdu: ")
    phone = input("Ievadiet tālruņa nr.: ")
    kontaktu_saraksts.append({"name": name, "phone": phone})
    print(f"✓ Pievienots: {name} ({phone})")
    return True

def list_contacts():
    """
    Parāda esošo kontaktu sarakstu
    """
    contacts = load_contacts()
    if not contacts:
        print("Saraksts ir tukšs.")
        return
    print("Kontakti:")
    # i ir skaitītājs, c is pati kontakta vārdnīca
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

def search_contacts(query):
    """
    Izveido jaunu sarkatu ar meklētajiem kontaktiem
    """
    contacts = load_contacts()
    # Izveidojam jaunu sarakstu tikai ar to kas atbilst meklētajam
    found = [c for c in contacts if query.lower() in c['name'].lower()]
    print(f"Atrasti {len(found)} kontakti:")
    for i, c in enumerate(found, 1):
        print(f"{i}. {c['name']} - {c['phone']}")

if __name__ == "__main__":
    kontaktu_saraksts = load_contacts()
    add_contacts(kontaktu_saraksts)
    save_contacts(kontaktu_saraksts)
    list_contacts()
    search_contacts("Artūrs")