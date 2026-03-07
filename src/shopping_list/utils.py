def calc_line_total(item):
    """
    Atgriež qty x price

    """
    return round(item.get('qty', 1) * item.get('price', 0), 2)

def calc_grand_total(items):
    """
    Summē visus line totals

    """
    return round(sum(calc_line_total(item) for item in items), 2)

def count_units(items):
    """
    Saskaita kopējo vienību skaitu (qty)
    
    """
    return sum(item.get('qty', 1) for item in items)
