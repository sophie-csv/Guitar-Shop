from flask import Flask
from model import guitar_shop_DAL as db
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

db.set_db()
add_category