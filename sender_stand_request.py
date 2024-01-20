import configuration
import requests
import data

# Создаем заказ
def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=body,
                         headers=data.headers)
new_order = create_new_order(data.order_body)

# Получаем номер заказа
def get_track_number(response):
    return response.json().get('track')
track_number = get_track_number(new_order)

#Получаем информацию о заказе по номеру
def get_order_info(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + f'?t={track_number}', headers=data.headers)