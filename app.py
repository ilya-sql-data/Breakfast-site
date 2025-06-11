from flask import Flask, render_template, request, redirect
from flask_caching import Cache
from models import OrderHandler
from menu import maindishs, coffees, fruits 
from telegram_bot import send_order_notification

app = Flask(__name__)

app.config['CACHE_TYPE'] = 'simple'
app.config['CACHE_DEFAULT_TIMEOUT'] = 300  # Исправлено имя параметра

cache = Cache(app)

#Создаем экземпляр класса для работы с заказами
order_handler = OrderHandler("orders.db")

@app.route('/')
@cache.cached(timeout=60)
def index():
    return render_template('index.html')

@app.route('/order', methods=('GET', 'POST'))
def order():
    if request.method == "POST":
        # Проверка на наличие всех обязательных полей
        required_fields = ['name', 'coffee', 'maindish', 'fruit']
        if not all(request.form.get(field) for field in required_fields):
            return "Ошибка: Все поля должны быть заполнены.", 400

        new_order = {
            "name": request.form.get('name'),
            "coffee": request.form.get('coffee'),
            "maindish": request.form.get('maindish'),
            "fruit": request.form.get('fruit')
        }

        try:
            order_handler.save_order(new_order)
            send_order_notification(new_order)
        except Exception as e:
            return f"Ошибка при обработке заказа: {e}", 500

        return render_template('print.html', new_order=new_order)

    return render_template('order.html', coffees=coffees, maindishs=maindishs, fruits=fruits)

@app.route("/list", methods =["GET"] )
@cache.cached(timeout=300)
def list_orders():
    sort = request.args.get("sort", "created_at_desc")
    date_filter = request.args.get("date")

    orders = order_handler.get_orders(sort, date_filter)
    return render_template("list.html", orders=orders)

if __name__ == '__main__':
   app.run(debug=True, host="0.0.0.0", port=5000)


