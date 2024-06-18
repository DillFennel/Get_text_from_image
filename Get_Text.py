from requests import get, ConnectionError
from PIL import Image, UnidentifiedImageError
from easyocr import Reader


reader = Reader(['ru', 'en']) 

def get_text_from_image(): #Считывает русский и английский текст c картинки.
    print("Введите ссылку на изображения в формате jpg или png или путь до него в файловой системе")
    img_path = input()
    if (img_path[:7] == "http://" or img_path[:8] == "https://"):
        print("Работаем с файлом в сети")
        try:
            from_url = get(img_path, stream=True).raw
            img = Image.open(from_url)
            print("Выводим картинку")
            img.show()
            text_from_file = reader.readtext(img_path, detail = 0) #Получаем текст из ссылки
        except ConnectionError:
            print("Ошибка соединения")
            return
        except UnidentifiedImageError:
            print("Не получается преобразовать данные в картинку. Возможно, ошибка в ссылке")
            return
    else:
        print("Работаем с локальный файлом")
        try:
            img = Image.open(img_path) #Открываем картинку
            print("Выводим картинку")
            img.show()
            text_from_file = reader.readtext(img_path, detail = 0) #Получаем текст из локального изображения
        except FileNotFoundError:
            print("Не найден такой файл")
            return
    print()
    print("Найденый текст:")
    for line in text_from_file:
        print(line)
    print()

get_text_from_image()
