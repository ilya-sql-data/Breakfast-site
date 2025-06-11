import os

def read_menu(filename):
    try:
        # Пытаемся открыть файл с указанным именем в кодировке cp1251 (часто используется для русского текста в Windows)
        full_path = os.path.join(os.path.dirname(__file__), filename)
        with open(full_path, encoding='utf-8') as f:
            # Считываем строки из файла, удаляем пробелы и переносы с краёв каждой строки, возвращаем как список
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Ошибка чтения {filename}: {e}")
        return []

maindishs = read_menu("maindishs.txt")
coffees = read_menu("coffees.txt")
fruits = read_menu("fruits.txt")

