from flask import Flask, render_template, request, redirect, jsonify, url_for

# TODO: Make everything else here even though you should try to spread out the classes. Reference the MUB project.

app = Flask(__name__)


@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/categories/')
def index():
    print("working?")
    # Show all categories
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/', methods=['GET', 'POST'])
def category():
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/items/', methods=['GET', 'POST'])
def category_items():
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/items/<int:item_id>/', methods=['GET', 'POST'])
def category_item():
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/items/new', methods=['GET', 'POST'])
def category_item_new():
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/items/<int:item_id>/update', methods=['GET', 'POST'])
def category_item_update():
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/items/<int:item_id>/delete', methods=['GET', 'POST'])
def category_item_delete():
    return render_template('index.html')
    pass


@app.route('/categories/new', methods=['GET', 'POST'])
def new_category():
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/edit', methods=['GET', 'POST'])
def edit_category():
    return render_template('index.html')
    pass


@app.route('/categories/<int:category_id>/delete', methods=['GET', 'POST'])
def delete_category():
    return render_template('index.html')
    pass


@app.route('/shops/', methods=['GET', 'POST'])
def shops():
    return render_template('index.html')
    pass


@app.route('/shops/<int:shop_id>/', methods=['GET', 'POST'])
def shop():
    return render_template('index.html')
    pass


@app.route('/shops/new', methods=['GET', 'POST'])
def shops_new():
    return render_template('index.html')
    pass


@app.route('/shops/<int:shop_id>/edit', methods=['GET', 'POST'])
def shops_update():
    return render_template('index.html')
    pass


@app.route('/shops/<int:shop_id>/delete', methods=['GET', 'POST'])
def shops_delete():
    return render_template('index.html')
    pass


@app.route('/manufacturers/', methods=['GET', 'POST'])
def manufacturers():
    return render_template('index.html')
    pass


@app.route('/manufacturers/<int:manufacturer_id>/', methods=['GET', 'POST'])
def manufacturer():
    return render_template('index.html')
    pass


@app.route('/manufacturers/new', methods=['GET', 'POST'])
def manufacturer_new():
    return render_template('index.html')
    pass


@app.route('/manufacturers/<int:manufacturer_id>/update', methods=['GET', 'POST'])
def manufacturer_update():
    return render_template('index.html')
    pass


@app.route('/manufacturers/<int:manufacturer_id>/delete', methods=['GET', 'POST'])
def manufacturer_delete():
    return render_template('index.html')
    pass


# Following routes are for creating a new entity from another page than the supposed one. Like from a 'New shop' button from the homepage.



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5050)
