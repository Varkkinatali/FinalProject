#Наташа Варкки, 12-я когорта — Финальный проект. Инженер по тестированию плюс

from sender_stand_request import create_new_order, get_track_number, get_order_info
import data
import pytest

# Тест создания заказа
def test_create_new_order():
    response = create_new_order(data.order_body)
    assert response.status_code == 201, "Ошибка при создании заказа"
    track_number = get_track_number(response)
    assert track_number is not None, "Номер трека не получен"
    return track_number

# Тест получения информации о заказе
def test_get_order_info():
    track_number = test_create_new_order()
    response = get_order_info(track_number)
    assert response.status_code == 200, "Ошибка при получении информации о заказе"