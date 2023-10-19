from flask import Flask, render_template
from blueprints.supermarket import supermarket
app = Flask(__name__)

app.register_blueprint(supermarket, url_prefix='/supermarket')

@app.route('/')
def main_menu():
    return render_template('index.html')

@app.route('/price')
def main_menu_price():
    return render_template('byprice.html')

@app.route('/category')
def main_menu_cat():
    return render_template('bycat.html')

if __name__ == '__main__':
    app.run()
