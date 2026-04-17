import requests

def send_order_notification(order):
    message = (
        f"Новый заказ!\n"
        f"Коммент: {order['name']}\n"
        f"Напиток: {order['coffee']}\n"
        f"Основное блюдо: {order['maindish']}\n"
        f"Фрукт: {order['fruit']}\n"
    )
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text":message}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка отправки уведомления: {e}")
