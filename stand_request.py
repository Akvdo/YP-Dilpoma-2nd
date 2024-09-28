# Александр Кравченко, 21-я когорта — Инженер по тестированию плюс - Дипломный проект - 2ая часть

# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL
import configuration

# Импорт данных из модуля data, в котором определены заголовки, тело запроса и значения переменных
import data

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт библиотеки pytest для выполнения автотестов

# Во всех запросах отключена проверка сертификатов "verify=False"
# Это позволяет избежать ошибок при перезапуске тестового-стенда,
# если что-то пошло не так с проверкой подлинности URL

# Определение функции post_new_user для отправки POST-запроса на создание нового пользователя
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers,
                         verify=False)

# Опредение функции get_new_user_token для подстановки в заголовок ключа "Authorization" c новым токеном "Bearer ###"
def get_new_user_token():
    response = post_new_user(data.user_body)
    current_headers = data.headers.copy()
    current_headers["Authorization"] = "Bearer " + response.json()["authToken"]
    return current_headers

# Переменная для хранения нового заголовка, в котором присутсвует токен
# Позволяет один раз создать нового пользователя и с ним выполнить 11 тестов
# Пользователь пересоздается каждый раз, когда перезапускаются тесты
new_user_headers = get_new_user_token()

# Определение функции get_kit_body, которая меняет значения ключа name
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Определение функции post_new_client_kit для создания нового набора нашего пользователя
def post_new_client_kit(body):
    return requests.post(configuration.URL_SERVICE + configuration.MAIN_KITS_PATH,
                        json=body,
                        headers=new_user_headers,
                        verify=False)


