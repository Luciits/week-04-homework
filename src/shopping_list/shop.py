import storage
import sys
import utils


def add_item(item, quantity, price):
    """
    Pievieno jaunu produktu produktu sarakstam.
    """
    shopping_list = storage.load_list()
    try:
        price = float(price)
        quantity = int(quantity)
        if quantity <= 0:
            print("Kļūda: Daudzumam jābūt vismaz 1!")
            return False
        new_item = {"item": item, "qty": quantity, "price": price}
        shopping_list.append(new_item)
        storage.save_list(shopping_list)
        print(f"✓ Pievienots: {item} x {quantity} ({price:.2f} EUR/gab) = {utils.calc_line_total(new_item):.2f}")
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
        print(f"{i}. {l['item']} x {l['qty']} - {l['price']:.2f} EUR/gab = {utils.calc_line_total(l):.2f} EUR")

def total_price():
    """
    Aprēķina kopējo iepirkumu summu.
    """
    shopping_list = storage.load_list()
    count = len(shopping_list)
    print(f"Kopējā summa: {utils.calc_grand_total(shopping_list):.2f} EUR ({count} produkti) ({utils.count_units(shopping_list)} vienības kopā)")


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
            if len(sys.argv) == 5:
                name = sys.argv[2]
                quantity = sys.argv[3]
                price = (sys.argv[4])
                add_item(name, quantity, price)
            else:
                print("Kļūda: add komandai vajag preci, daudzumu un cenu!")
                print("Piemērs: python shop.py add Maize 3 1.20")
        elif command == "list":
            list_item()
        elif command == "total":
            total_price()
        elif command == "clear":
            clear_list()
        else:
            print(f"Nezināma komanda: {command}")