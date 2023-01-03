import datetime
import json

TAX = .0875

def _gross_item_total(items: list) -> float:
        return 123.48

class Reciepts:
    def __init__(self, id: int, items: list, server_id: int) -> None:
        self.id = id
        self.items = items
        self.gross = _gross_item_total(items)
        self.tax = round(self.gross * TAX, 2)
        self.total = self.gross + self.tax
        self.server_id = server_id
        self.time = datetime.datetime.now()
        
    def _get_dict(self):
        return {x: getattr(self, x) for x in dir(self) if not x[0] == "_"}
