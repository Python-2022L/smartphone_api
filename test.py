from smartphonedb import SmatrphoneDb
db=SmatrphoneDb()
def get_1():
    return db.get_brand()
print(get_1())
def get_2():
    """Get all grocery by type"""
    return db.get_product_by_brand("Apple")
#print(get_2())
def get_3():
    """Get all grocery by type"""
    return db.get_price('Apple',315.3)
#print(get_3())
def get_4():
    return db.get_product('Apple','Apple iPhone XR')
print(get_4())
