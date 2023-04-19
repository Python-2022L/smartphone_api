from tinydb import TinyDB,Query
import json

class SmatrphoneDb:
    def __init__(self,path) -> None:
        self.db = TinyDB(path, indent=4, separators=(',', ': '))
        self.query = Query()

    def get_brand(self):
        return self.db.tables()

    def get_product_by_brand(self, brand):
        table = self.db.table(brand)
        return table.all()

    def get_product(self, brand, id): 
        table = self.db.table(brand)
        brendcha=table.get(doc_id=id)
        return brendcha