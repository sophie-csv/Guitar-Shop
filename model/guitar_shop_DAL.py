import json


def set_db():
    init_db = {
        "Guitars": {
            "strat": {
                "name": "Fender Stratocaster",
                "price": 699.0
            },
            "les_paul": {
                "name": "Gibson Les Paul",
                "price": 799.99
            },
            "sg": {
                "name": "Gibson SG",
                "price": 1234.0
            },
            "fg700s": {
                "name": "Fender FG700S",
                "price": 1399.99
            }
        },
        "Basses": {
            "precision": {
                "name": "Fender Precision",
                "price": 999.0
            },
            "hofner": {
                "name": "Hofner Icon",
                "price": 499.99
            }
        },
        "Drums": {
            "ludwig": {
                "name": "Ludwig 5-piece Drum Set with Cymbals",
                "price": 699.99
            },
            "tama": {
                "name": "Tama 5-Piece Drum Set with Cymbals",
                "price": 799.99
            }
        }
    }
    f = open('database/guitar_shop_DB.json', 'w')
    json.dump(init_db, f)
    f.close()

def get_db_as_dict():
    f = open('database/guitar_shop_DB.json', 'r')
    data = json.load(f)
    f.close()
    return data

def write_to_db(data):
    f = open('database/guitar_shop_DB.json', 'w')
    json.dump(data, f)
    f.close()

def add_category(category):
    data = get_db_as_dict()
    data[category] = {}
    write_to_db(data)

def delete_category(category):
    data = get_db_as_dict()
    del data[category]
    write_to_db(data)

def get_category(category):
    data = get_db_as_dict()
    return data[category]

def get_all_categories_as_list():
    data = get_db_as_dict()
    return list(data)

def add_product(category,code,name,price):
    data = get_db_as_dict()
    data[category][code] = {
        "name": name,
        "price": price
    }
    write_to_db(data)

def delete_product(category,code):
    data = get_db_as_dict()
    del data[category][code]
    write_to_db(data)

#has subpoints, multiple keys
def get_all_products_in_category(category):
    data = get_db_as_dict()
    return data[category]

def get_product_name(category, code):
    data = get_db_as_dict()
    return data[category][code]

def get_product_price(category, code):
    data = get_db_as_dict()
    return data[category][code]['price']