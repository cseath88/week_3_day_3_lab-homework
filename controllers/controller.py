from app import app
from flask import render_template
from models.orders import order_list

@app.route('/orders')
def index():
    return render_template('index.jinja', title = 'Home', orders = order_list)

@app.route('/orders/<index>')
def get_index(index):
    index = order_list[int(index)]
    return render_template('order.jinja', title = 'Order', order=id) 