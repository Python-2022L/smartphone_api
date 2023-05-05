from flask import Flask,request
from smartphonedb import SmatrphoneDb
from cartdb import CartDb
app = Flask(__name__)
db=SmatrphoneDb('smartphone_api/db.json')
add_cards=CartDb()

#1
@app.route('/smartphone')
def get_brand1():
    """Get all grocery by type"""
    #table = db.get_brand()
    return {"Brands": list(db.get_brand())}

#2
@app.route('/smartphone/<brand>')
def get_product_by_brand1(brand):
    """Get all grocery by type"""
    return {"products": db.get_product_by_brand(brand=brand)}
#3
@app.route('/smartphone/<brand>/<int:idx>')
def getPhone(brand,idx) -> dict:
    """
    Return phone data by brand
    """
    return {"product": db.get_product(brand=brand,id=idx)}

#4
@app.route('/smartphone/<brand>',methods=['POST'])
def addPhone(brand) -> dict:
    """
    Add new phone to the database
    """
    all_table = db.get_brand()
    if brand in all_table:
        data = request.get_json()
        table = db.db.table(brand)
        table.insert(data)
        return {"status":"success"}
    else:
        return {"status":"failed","message":"Brand not found"}

@app.route('/smartphone/add',methods=['POST'])  
def add():
    data = request.get_json()
    chat_id=data['chat_id']
    product_id=data['product_id']
    company=data['company']
    add_cards.add_order(chat_id=chat_id,product_id=product_id,company=company)
    return {"status":"success"}

@app.route('/smartphone/getorder/<chat_id>')
def get_ord(chat_id)->dict:
    return {"get_order": add_cards.get_order(chat_id=int(chat_id))}

@app.route('/smartphone/clearorder',methods=['POST'])
def clear():
    data = request.get_json()
    chat_id=data['chat_id']
    add_cards.clear_order(chat_id=chat_id)
    return {"status":"success"}
if __name__ == '__main__':
    app.run(debug=True)
