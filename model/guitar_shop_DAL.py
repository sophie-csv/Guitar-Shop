import json

"""
Sets up the initial database.
"""
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

"""
Loads the database from a json file and returns it as a dict to use in other methods.
"""
def get_db_as_dict():
    f = open('database/guitar_shop_DB.json', 'r')
    data = json.load(f)
    f.close()
    return data

"""
Writes to the database and adds it to the file. 
"""
def write_to_db(data):
    f = open('database/guitar_shop_DB.json', 'w')
    json.dump(data, f)
    f.close()

"""
Adds a category to the database and adds it to the file.
Category: Category to add
"""
def add_category(category):
    data = get_db_as_dict()
    data[category] = {}
    write_to_db(data)

"""
Deletes a category to the database and remove it to the file.
Category: Category to delete
"""
def delete_category(category):
    data = get_db_as_dict()
    del data[category]
    write_to_db(data)

"""
Returns all categories as a list
"""
def get_all_categories_as_list():
    data = get_db_as_dict()
    return list(data)
"""
Adds a product to the database and adds it to the file.
Category: Category to add
Code: Code to identify
Name: Name to identify
Price: Price to identify
"""
def add_product(category,code,name,price):
    data = get_db_as_dict()
    data[category][code] = {
        "name": name,
        "price": price
    }
    write_to_db(data)

"""
Deletes a product to the database and removes it to the file.
Category: Category to add
Code: Code to identify
Name: Name to identify
Price: Price to identify
"""
def delete_product(category,code):
    data = get_db_as_dict()
    del data[category][code]
    write_to_db(data)

"""
Gets all categories from a specified category and returns it.
Category: Category to get
"""
def get_all_products_in_category(category):
    data = get_db_as_dict()
    return data[category]
"""
Gets a product name from a specified category and code and returns it.
Category: Category to get
Code: Code to identify
"""
def get_product_name(category, code):
    data = get_db_as_dict()
    return data[category][code]

"""
Get a product price from a specified category and code and returns it.
Category: Category to get
Code: Code to identify
"""
def get_product_price(category, code):
    data = get_db_as_dict()
    return data[category][code]['price']