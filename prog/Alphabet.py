alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
            'Ф',
            'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']


def encryptCaesar(key, text):
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    # Создаем алфавит
    message = text
    smeshenie = key
    itog = ''

    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto + smeshenie
        if i in alfavit:
            itog += alfavit[new_mesto]  # Задаем значения в итог
        else:
            itog += i
    print(itog)
    return ''.join(itog)


def decryptCaesar(key, text):
    alfavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    # Создаем алфавит
    message = text
    smeshenie = key
    itog = ''
    for i in message:
        mesto = alfavit.find(i)
        new_mesto = mesto - smeshenie
        if i in alfavit:
            itog += alfavit[new_mesto]  # Задаем значения в итог
        else:
            itog += i
    print(itog)
    return ''.join(itog)