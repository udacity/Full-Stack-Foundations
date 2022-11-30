from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dbmodels import Base, Shop, Item, Manufacturer, Category

# TODO: Make everything else here even though you should try to spread out the classes. Reference the MUB project.

app = Flask(__name__)

engine = create_engine('sqlite:///models.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
sess = DBSession()


@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/categories/')
def index():
	print("You are logged, muhahaha!")
	# Show all categories
	categories = sess.query(Category).all()
	return render_template('index.html', category=categories)
	pass


@app.route('/categories/<int:category_id>/', methods=['GET', 'POST'])
def category(category_id):
	categoriess = sess.query(Category).all
	return render_template('category.html', categories=categoriess)
	pass


@app.route('/categories/<int:category_id>/items/', methods=['GET', 'POST'])
def category_items(category_id):
	return render_template('index.html')
	pass


@app.route('/categories/<int:category_id>/items/<int:item_id>/', methods=['GET', 'POST'])
def category_item(category_id, item_id):
	return render_template('index.html')
	pass


@app.route('/categories/<int:category_id>/items/new', methods=['GET', 'POST'])
def category_item_new(category_id):
	return render_template('index.html')
	pass


@app.route('/categories/<int:category_id>/items/<int:item_id>/update', methods=['GET', 'POST'])
def category_item_update(category_id, item_id):
	return render_template('index.html')
	pass


@app.route('/categories/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def category_item_delete(category_id, item_id):
	return render_template('index.html')
	pass


@app.route('/category/new', methods=['GET', 'POST'])
def new_category():
	return render_template('index.html')
	pass


@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def edit_category(category_id):
	return render_template('index.html')
	pass


@app.route('/category/<int:category_id>/delete', methods=['GET', 'POST'])
def delete_category(category_id):
	return render_template('index.html')
	pass


@app.route('/shops/', methods=['GET', 'POST'])
def shops():
	return render_template('index.html')
	pass


@app.route('/shops/<int:shop_id>/', methods=['GET', 'POST'])
def shop(shops_id):
	return render_template('index.html')
	pass


@app.route('/shop/new', methods=['GET', 'POST'])
def shops_new():
	return render_template('index.html')
	pass


@app.route('/shop/<int:shop_id>/edit', methods=['GET', 'POST'])
def shops_update(shops_id):
	return render_template('index.html')
	pass


@app.route('/shop/<int:shop_id>/delete', methods=['GET', 'POST'])
def shops_delete(shops_id):
	return render_template('index.html')
	pass


@app.route('/manufacturers/', methods=['GET', 'POST'])
def manufacturers():
	return render_template('index.html')
	pass


@app.route('/manufacturers/<int:manufacturer_id>/', methods=['GET', 'POST'])
def manufacturer(manufacturer_id):
	return render_template('index.html')
	pass


@app.route('/manufacturer/new', methods=['GET', 'POST'])
def manufacturer_new():
	return render_template('index.html')
	pass


@app.route('/manufacturer/<int:manufacturer_id>/update', methods=['GET', 'POST'])
def manufacturer_update(manufacturer_id):
	return render_template('index.html')
	pass


@app.route('/manufacturer/<int:manufacturer_id>/delete', methods=['GET', 'POST'])
def manufacturer_delete(manufacturer_id):
	return render_template('index.html')
	pass
"""
To actually be able to read from a database, remember to use id's AND call them, use unique naming whenever possible.

Conclusion of routes, add additional routes above this comment.
"""

# Standard convention. Call if this is run as the main module.
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5050)
