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
    data