# Импортируем модуль sender_stand_request, содержащий функции для отправки HTTP-запросов к API.
import sender_stand_request
# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data

# Позитивные проверки
def positive_assert(kit_body):
    new_kit = sender_stand_request.get_kit_body(kit_body)
    new_response = sender_stand_request.post_new_client_kit(new_kit)
    # Проверяется, что код ответа равен 201
    assert new_response.status_code == 201
    # Проверяется, что в ответе есть поле authToken и оно не пустое
    assert new_response.json()["name"] == kit_body

# Негативные проверки
def negative_assert_code_400(kit_body):
    new_kit = sender_stand_request.get_kit_body(kit_body)
    new_response = sender_stand_request.post_new_client_kit(new_kit)
    # Проверяется, что код ответа равен 400
    assert new_response.status_code == 400

# Тест № 1 - Допустимое количество символов (1) - "а"
def test_create_kit_1_letter_in_name():
    positive_assert("а")

# Тест № 2 - Допустимое количество символов (511)
# Тестовое значение для этой проверки сохранено в data.py
def test_create_kit_511_letter_in_name():
    positive_assert(data.name_test2)

# Тест № 3 - Количество символов меньше допустимого (0) - ""
def test_create_kit_0_letter_in_name():
    negative_assert_code_400("")

# Тест № 4 - Количество символов больше допустимого (512)
# Тестовое значение для этой проверки сохранено в data.py
def test_create_kit_512_letter_in_name():
    negative_assert_code_400(data.name_test4)

# Тест № 5 - Разрешены английские буквы - "QWErty"
def test_create_kit_en_letter_in_name():
    positive_assert("QWErty")

# Тест № 6 - Разрешены русские буквы - "Мария"
def test_create_kit_ru_letter_in_name():
    positive_assert("Мария")

# Тест № 7 - Разрешены спецсимволы - ""№%@","
def test_create_kit_special_char_in_name():
    positive_assert("\"№%@\",")

# Тест № 8 - Разрешены пробелы - " Человек и КО "
def test_create_kit_spaces_in_name():
    positive_assert(" Человек и КО ")

# Тест № 9 - Разрешены цифры - "123"
def test_create_kit_digit_in_name():
    positive_assert("123")

# Тест № 10 - Параметр name не передан в запросе
def test_create_kit_no_name():
    current_body = data.kit_body.copy()
    current_body.pop("name")
    negative_assert_code_400(current_body)

# Тест № 11 - Передан другой тип параметра (число) - 123
def test_create_kit_name_is_digit():
    negative_assert_code_400(123)