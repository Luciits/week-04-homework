import storage
import sys


def add_item(item, price):
    """
    Pievieno jaunu produktu produktu sarakstam.
    """
    shopping_list = storage.load_list()
    try:
        price = float(price)
        shopping_list.append({"item": item, "price": price})
        storage.save_list(shopping_list)
        print(f"✓ Pievienots: {item} ({price:.2f} EUR)")
        return True
    except ValueError:
        print("Kļūda: Cena nav derīgs skaitlis! Mēģiniet vēlreiz.")
        return False

def list_item():
    """
    Parāda esošo iepirkumu sarakstu
    """
    shopping_list = storage.load_list()
    if not shopping_list:
        print("Iepirkumu saraksts ir tukšs!")
        return
    print("\nIepirkumu saraksts:")
    for i, l in enumerate(shopping_list, 1):
        print(f"{i}. {l['item']} - {l['price']}")

def total_price():
    """
    Aprēķina kopējo iepirkumu summu.
    """
    shopping_list = storage.load_list()
    summa = 0.0
    item_count = len(shopping_list)
    for shop in shopping_list:
        summa += shop['price']
    print(f"Kopējā summa: {summa:.2f} EUR ({item_count} produkti)")


def clear_list():
    """
    Nodzēš iepirkumu sarakstu un saglabā tukšu sarakstu.
    """
    empty_list = []
    storage.save_list(empty_list)
    print("✓ Iepirkumu saraksts ir notīrīts!")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Lietošana: python shop.py [add/list/total/clear]")
    else:
        command = sys.argv[1]
        if command == "add":
            if len(sys.argv) == 4:
                name = sys.argv[2]
                price = (sys.argv[3])
                add_item(name, price)
            else:
                print("Kļūda: add komandai vajag preci un cenu!")
                print("Piemērs: python sjop.py add Maize 1.20")
        elif command == "list":
            list_item()
        elif command == "total":
            total_price()
        elif command == "clear":
            clear_list()
        else:
            print(f"Nezināma komanda: {command}")