import csv
from pathlib import Path

from flask import Flask, render_template, url_for
from flask_app_creator import FlaskAppCreator

app = FlaskAppCreator.create()


def read_products():
    file_path = Path(app.static_folder) / "csv" / "products.csv"
    items = []
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            items.append({
                'title': row[0],
                'description': row[1],
                'price': float(row[2]),
                'rating': float(row[3]),
                'image': row[4]
            })
    return items


@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route("/products", methods=['GET', 'POST'])
def products():
    products = read_products()
    return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
