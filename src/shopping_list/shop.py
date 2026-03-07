import sys
import storage
import utils

def handle_add(args):
    if len(args) < 2:
        print("Kļūda: Trūkst argumentu. Lietošana: add [nosaukums] [daudzums] (cena)")
        return

    name = args[0]
    try:
        qty = int(args[1])
        if qty <= 0: raise ValueError
    except (ValueError, IndexError):
        print("Kļūda: Daudzumam jābūt pozitīvam veselam skaitlim.")
        return

    # 3. soļa loģika: Cenu meklēšana
    price = storage.get_price(name)
    
    if price is not None:
        print(f"Atrasta cena: {price:.2f} EUR/gab.")
        choice = input("[A]kceptēt / [M]ainīt? > ").strip().upper()
        if choice == 'M':
            try:
                price = float(input("Jaunā cena: > "))
                if price <= 0: raise ValueError
                storage.set_price(name, price)
                print(f"✓ Cena atjaunināta: {name} → {price:.2f} EUR")
            except ValueError:
                print("Kļūda: Nederīga cena.")
                return
    else:
        # Ja cena nav zināma
        try:
            print("Cena nav zināma.")
            price = float(input("Ievadi cenu: > "))
            if price <= 0: raise ValueError
            storage.set_price(name, price)
            print(f"✓ Cena saglabāta: {name} ({price:.2f} EUR)")
        except ValueError:
            print("Kļūda: Nederīga cena.")
            return

    # Saglabāšana sarakstā
    items = storage.load_list()
    items.append({"name": name, "qty": qty, "price": price})
    storage.save_list(items)
    
    line_total = utils.calc_line_total({"qty": qty, "price": price})
    print(f"✓ Pievienots: {name} × {qty} ({price:.2f} EUR/gab.) = {line_total:.2f} EUR")

def handle_list():
    items = storage.load_list()
    if not items:
        print("Iepirkumu saraksts ir tukšs.")
        return
    print("Iepirkumu saraksts:")
    for i, item in enumerate(items, 1):
        line_total = utils.calc_line_total(item)
        print(f"  {i}. {item['name']} × {item['qty']} — {item['price']:.2f} EUR/gab. — {line_total:.2f} EUR")

def handle_total():
    items = storage.load_list()
    total = utils.calc_grand_total(items)
    units = utils.count_units(items)
    print(f"Kopā: {total:.2f} EUR ({units} vienības, {len(items)} produkti)")

def handle_clear():
    storage.save_list([])
    print("✓ Saraksts notīrīts.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Komandas: add, list, total, clear")
        sys.exit(1)

    cmd = sys.argv[1].lower()
    if cmd == "add":
        handle_add(sys.argv[2:])
    elif cmd == "list":
        handle_list()
    elif cmd == "total":
        handle_total()
    elif cmd == "clear":
        handle_clear()
    else:
        print("Nezināma komanda.")