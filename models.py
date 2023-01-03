import datetime
import json

TAX = .0875

def _gross_item_total(items: list) -> float:
        return 123.48


class common:
    def _get_dict(self):
        return {x: getattr(self, x) for x in dir(self) if not x[0] == "_" and not 'get' in x}


class Reciepts(common):
    def __init__(self, id: int, items: list, server_id: int) -> None:
        self.id = id
        self.items = items
        self.gross = _gross_item_total(items)
        self.tax = round(self.gross * TAX, 2)
        self.total = self.gross + self.tax
        self.server_id = server_id
        self.time = datetime.datetime.now()
    
    
class RecieptItem(common):
    def __init__(self, id: int, price: float, recipe: list) -> None:
        self.id = id
        self.price = price
        self.recipe = recipe


class Recipe(common):
    def __init__(self, id: int, price: float, recipe: list) -> None:
        self.id = id
        self.price = price
        self.recipe = recipe

class BOH_Item(common):
    def __init__(self, id: int, price: float) -> None:
        self.id = id
        self.price_per_unit = price

class Server(common):
    def __init__(self, id: int, name: str, born: datetime, hire_date: datetime) -> None:
        self.id = id
        self.name = name
        self.born = born
        self.hire_date = hire_date