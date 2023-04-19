from tinydb import TinyDB, Query
class CartDb:

    def __init__(self):
        self.order_db = TinyDB('cart.json', indent=4)
        self.query=Query()
       
    
    def add_order(self, chat_id: str, product_id: str, company: str):
        order = self.order_db.get((self.query.chat_id == chat_id) & (self.query.company == company) & (self.query.product_id == product_id))
        if order:
            order['quantity'] += 1
            return self.order_db.update(order, (self.query.chat_id == chat_id) & (self.query.company == company) & (self.query.product_id == product_id))
        order = {
            'chat_id': chat_id,
            'product_id': product_id,
            'company': company,
            'quantity': 1
        }
        return self.order_db.insert(order)

    def get_order(self, chat_id: int):
        orders=self.order_db.search(self.query.chat_id ==chat_id)
        return orders
    

    def clear_order(self, chat_id: int):
        return self.order_db.remove(self.query.chat_id == chat_id)