from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

database = 'products.db'


@app.route('/')
def show_categories():
    categories = []
    con = sqlite3.connect(database)
    con.row_factory = sqlite3.Row

    cur = con.cursor()
    cur.execute('SELECT name FROM categories')
    for row in cur:
        categories.append(row)

    con.close()

    return render_template('index.html', categories=categories)


@app.route('/<category>')
def show_product_list(category):
    products_list = []
    con = sqlite3.connect(database)
    cur = con.cursor()
    category_id = (cur.execute('SELECT category_id FROM categories WHERE name = ?', [category])).fetchone()

    products = (cur.execute('SELECT products.name, product_id '
                            'FROM products '
                            'INNER JOIN categories on products.category = categories.category_id '
                            'WHERE products.category = ?', [category_id[0]])).fetchall()

    for product in products:
        product_details = {
            'name': product[0],
            'product_id': product[1]
        }
        products_list.append(product_details)

    con.close()

    return render_template('product_list.html', products_list=products_list)


@app.route('/product/<_id>')
def show_product_details(_id):
    con = sqlite3.connect(database)
    cur = con.cursor()
    sql_query = 'SELECT products.name, in_stock, price, qty, categories.name ' \
                'FROM products ' \
                'INNER JOIN categories on products.category = categories.category_id ' \
                'WHERE product_id = ?'
    product = cur.execute(sql_query, [_id])
    return render_template('product_details.html', product=product)


if __name__ == '__main__':
    app.run(debug=True)
