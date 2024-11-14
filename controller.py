from flask import Flask, request, render_template, redirect, url_for

from model import guitar_shop_DAL as db

app = Flask(__name__, template_folder='view/templates', static_folder='view/static')


@app.route('/', methods=['GET']) # get can bookmark
def index():
    category_key = request.args.get('category_key')

    category_list = db.get_all_categories_as_list()

    if category_key is None or category_key not in category_list:
        category_key = category_list[0]
        return redirect(url_for('index', category_key=category_key))

    product_list = db.get_all_products_in_category(category_key)

    return render_template('index.html',
                           category_key=category_key,
                           category_list=category_list,
                           product_list=product_list)


@app.route('/add_product_form')
def show_product_form():
    category_list = db.get_all_categories_as_list()
    return render_template('add_product_form.html', category_list=category_list)


@app.route('/add_product', methods=['POST'])
def add_product():
    category_key = request.form.get('category_key')
    code = request.form.get('code')
    name = request.form.get('name')
    price = request.form.get('price')

    if name == '' or code == '' or price == '':
        return render_template('error.html',
                               error='Invalid product data. Check all fields and try again.')

    db.add_product(category_key, code, name, price)
    return redirect(url_for('index', category_key=category_key))


@app.route('/delete_product', methods=['POST'])
def delete_product():
    category_key = request.form.get('category_key')
    product_code = request.form.get('product_code')
    db.delete_product(category_key, product_code)
    return redirect(url_for('index', category_key=category_key))


@app.route('/category_list', methods=['GET'])
def category_list():
    category_list = db.get_all_categories_as_list()
    return render_template('category_list.html', category_list=category_list)


@app.route('/add_category', methods=['POST'])
def add_category():
    category_key = request.form.get('category')
    db.add_category(category_key)
    return redirect(url_for('category_list', category_key=category_key))


@app.route('/delete_category', methods=['POST'])
def delete_category():
    category_key = request.form.get('category_key')
    if db.get_all_products_in_category(category_key) == {}:
        db.delete_category(category_key)
        return redirect(url_for('category_list'))
    else:
        return render_template("error.html", error="Category has products.")


if __name__ == '__main__':
    app.run()
