# Александр Кравченко, 21-я когорта — Инженер по тестированию плюс - Дипломный проект - 2ая часть

# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL
import configuration

# Импорт данных из модуля data, в котором определены заголовки, тело запроса и значения переменных
import data

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Определение функции create_new_order для отправки POST-запроса на создание нового заказа
# Функция возвращает трек нового заказа
def create_new_order():
    response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body,
                         headers=data.headers)
    return response.json()["track"]

# Переменная для хранения трека нового заказа
current_track = create_new_order()

# Определение функции check_new_order для отправки GET-запроса для проверки заказа по его треку
# При этом трек преобразуется в строку и затем подставляется в URL
# Функция возвращает код ответа после проверки нового заказа по его треку
def check_new_order(track):
    response = requests.get(configuration.URL_SERVICE + configuration.CHECK_ORDER_PATH + str(track))
    return response.status_code

# Тест test_status_code для проверки, что по треку заказа можно получить данные о заказе
def test_new_order_check_status_code():
     # Проверяется, что код ответа равен 200
     assert check_new_order(current_track) == 200

