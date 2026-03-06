def calc_line_total(item):
    """
    Aprēķina vienas preces kopējo summu (daudzums x cena)
    """
    total = item['qty'] * item['price']
    return total

def calc_grand_total(items):
    """
    Aprēķina visa sarakta kopējo summu.
    """
    grand_total = 0.0
    for item in items:
        grand_total += calc_line_total(item)
    return grand_total

def count_units(items):
    """
    Saskaita kopējo preču skaitu visā sarakstā.
    """
    total_units = 0
    for item in items:
        total_units += item['qty']
    return total_units

if __name__ == "__main__":
    # Testa saraksts ar paraug datiem
    test_list = [{'item': 'Piens', 'qty': 2, 'price': 1.50},{'item': 'Maize', 'qty': 1, 'price': 1.20}]
    # Tests vienas rindas aprēķins
    print(f'Testa rindas summa: {calc_line_total(test_list[0])}')
    # Tests kopējā summa
    print(f'Tests kopējā summa: {calc_grand_total(test_list)}')
    # Tests kopējo produktu skaits
    print(f'Tests kopējais produktu skaits: {count_units(test_list)}')
