"""

Тестовое задание - Телефонный справочник

"""

from typing import NoReturn
from lists import human_params, which_cmd
import sys


def text_highlighter(imp_str: str = "") -> str:
    """ФУНКЦИЯ, КОТОРАЯ ДЕЛАЕТ ТЕКСТ ЖИРНЫМ"""
    return "\033[1m{}\033[0m".format(imp_str)

# Главное меню
def welcome(which_cmd: list[str] = which_cmd) -> NoReturn:
    """ФУНКЦИЯ-МЕНЮ"""

    ### Приветственная надпись
    counter = 0
    print("\n" + "#" * 100 + "\n")
    print(text_highlighter("ГЛАВНОЕ МЕНЮ:"))
    print("\n")

    for i in range(5):
        print(f"{i+1} - {which_cmd[i]}")

    print("\n")
    user_ans = int(
        input(text_highlighter("Какой командой желаете восьпользоваться? => ").strip())
    )
    print("\n")
    ###

    # Варианты функций
    match user_ans:
        case 1:
            page_by_page()

        case 2:
            add_human()
        case 3:
            edit_contact()

        case 4:
            s = find_human(response=[], counter=0)
            print('\n')
            print('Пользователи подходящие под ваше описание:')
            for i in range(len(s)):
                print(text_highlighter(s[i]))
            wanna_cont = input(
                text_highlighter(
                    "Если хотите вернуться в главное меню нажмите 1, завершить программу - любая другая кнопка => "
                ).strip()
            )

            welcome() if wanna_cont == "1" else sys.exit()

        case 5:
            sys.exit()
        case _:
            print(text_highlighter("Такой команды не существует :9"))
            welcome()




# Функция добавления пользователя


def add_human(human_params: list[str] = human_params) -> str:
    """ФУНКЦИЯ ПОЛУЧАЕТ ЗАПРАШИВАЕТ ДАННЫЕ, КОТОРЫЕ НУЖНО ВНЕСТИ И ЗАПИСЫВАЕТ ИХ В СТРОЧКУ В ФАЙЛЕ"""

    human = []

    for param in human_params:
        human.append(input(f'Введите поле "{text_highlighter(param.upper())}" => ').strip().replace(" ","-"))

    with open(file="catalog.txt", mode="a+", encoding="utf-8") as catalog:

        catalog.seek(0, 2)

        if len(catalog.readlines()) > 0:
            catalog.write("\n")

        catalog.write(" ".join(human) + "\n")

        print(f"\n{text_highlighter("КОНТАКТ УСПЕШНО ДОБАВЛЕН!!!")}\n")

    wanna_cont = input(
                text_highlighter(
                    "Если хотите вернуться в главное меню нажмите 1, завершить программу - любая другая кнопка => "
                ).strip()
            )

    welcome() if wanna_cont == "1" else ...


# Функция поиска человека


def find_human(
    response: list[str] = [],
    counter: int = 0,
    finding_options: list[str] = human_params,
) -> list[str]:
    """ФУНКЦИЯ ПОЛУЧАЕТ ПОЛЕ/Я И ОТВЕТ/Ы К НЕМУ/ИМ ПО КОТОРЫМ НУЖНО ИСКАТЬ НУЖНОГО ЧЕЛОВЕКА
    КАЖДАЯ СТРОЧКА РАЗРЕЗАЕТСЯ НА СОСТАВЛЯЮЩИЕ И ЗАТЕМ В ЦИКЛЕ ЭТИ ЗАНЧЕНИЯ СРАВНИВАЮТСЯ С
    ОЖИДАЕМЫМИ.
    """
    ################### Вывод вариантов ответов
    try:
        with open(file="catalog.txt",mode='r',encoding='utf-8'):
            ...
    except:
        print(text_highlighter("КАТАЛОГ ПОКА ЧТО ПУСТ!"))
        welcome()
    
    print(f"{text_highlighter("По какому признаку будем искать пользователя?")}\n")
    for i in range(6):
        print(f"{i+1} - {finding_options[i]}")

    print("\n")
    ###################

    # Ответ на то, какой вариант/ы поиска нужен/ы
    user_answer = list(
        map(int, input(text_highlighter("Введите через пробел вариант/ы поиска => ")).split())
    )
    if any(int(i) > 6 for i in user_answer):
        print(text_highlighter("ТАКОГО ВАРИАНТА НЕТ"))
        find_human(response=[],counter=0)
    # Словарь для предпочтительных ответов
    desired_answeres = dict()

    # Заполнение словаря
    for k in user_answer:
        ans = input(f'Введите поле "{text_highlighter(finding_options[k-1]).strip()}" => ')
        desired_answeres[finding_options[k - 1]] = ans

    # Работа с файлом
    try:
        with open(file="catalog.txt", encoding="utf-8", mode="r") as catalog:

            # Поиск человека

            for line in catalog.readlines():
                elements_of_working_line = line.split()

                for answer in user_answer:
                    if (
                        elements_of_working_line[answer - 1].strip()
                        == desired_answeres[finding_options[answer - 1]].strip()
                    ):
                        counter += 1
                    else:
                        counter = 0

                if counter == len(user_answer):
                    counter = 0
                    response.append(line)
    except:
        print(text_highlighter("КАТАЛОГ ПОКА ЧТО ПУСТ!"))
    return response


# Функция редактирования контакта


def edit_contact(human_params: list[str] = human_params) -> NoReturn:
    """ФУНКЦИЯ ЗАПРАШИВАЕТ ПАРАМЕТРЫ КОНТАКТА, КОТОРЫЙ НУЖНО ИЗМЕНИТЬ,
    ИЩЕТ НУЖНОГО ПОЛЬЗОВАТЕЛЯ, ЗАПРАШИВАЕТ ПОЛЯ КОТОРЫЕ НУЖНО ИЗМЕНИТЬ И В ЦИКЛЕ ПОЛУЧАЕТ
    НУЖНЫЕ ЗНАЧЕНИЕ, ЗАТЕМ СТАРУЮ СТРОКУ ЗАМЕНЯЕТ НОВОЙ В СПИСКЕ, ЗАТЕМ ЭТОТ СПИСОК СТРОК
    ВНОСИТСЯ В ФАЙЛ
    """

    line = find_human(response=[], counter=0)

    ### Сбор данных от пользователя
    if len(line) == 1:
        print('\n')
        print(f"{text_highlighter("Что хотите изменить?")}\n")
        for i in range(len(human_params)):
            print(f"{i+1} - {human_params[i]}")
        print("\n")

        user_answer = list(
            map(
                int,
                input(text_highlighter("Введите через пробел поля, которые нужно заменить => ")).split(),
            )
        )


        if any(int(i) > 6 for i in user_answer):
            print(text_highlighter("ТАКОГО ВАРИАНТА НЕТ"))
            edit_contact()
        new_line = line[0].split()
        for j in user_answer:
            new_line[j - 1] = input(f'Введите поле "{text_highlighter(human_params[j-1])}" => ').strip()
        ###

        new_line = " ".join(new_line) + "\n"

    
    
        # Формирование нужной строки
        with open(file="catalog.txt", encoding="utf-8", mode="r") as catalog:
            list_of_catalog = catalog.readlines()
            for i in range(len(list_of_catalog)):
                if list_of_catalog[i].strip() == line[0].strip():
                    list_of_catalog[i] = new_line
                    break

        # Внос изменений в файл
        with open(file="catalog.txt", encoding="utf-8", mode="w") as catalog:
            catalog.writelines(list_of_catalog)
            print(text_highlighter("УСПЕШНО!"))
            print('\n')

        wanna_cont = input(text_highlighter(
        "Если хотитет внести еще изменения нажмите 1, вернуться в главное меню - любая другая кнопка => "
        ).strip())

        edit_contact() if wanna_cont == "1" else welcome()

        
         

        
        

    elif len(line) > 1:
        print(text_highlighter(
            "Под данное описание подходит несколько контактов, если хотите изменить какую-то запись укажите более подробное описание!"
        ))
        edit_contact()

    else:
        print('\n')
        print(text_highlighter("Ни одной записи не нашлось :("))
        print('\n')
        print(text_highlighter("Попробуйте найти с другими параметрами!"))
        print('\n')
        edit_contact()


# Функция постраничного вывода контактов


def page_by_page() -> NoReturn:
    """СОЗДАЮТСЯ ФАЙЛЫ, В КАЖДОМ ИЗ КОТОРЫХ ПО ОДНОМУ ПОЛЬЗОВАТЕЛЮ"""
    line = []
    try:
        with open(file="catalog.txt", encoding="utf-8", mode="r") as file:
            line = file.readlines()

        for i in range(len(line)):
            with open(
                file=f"one_record_{i+1}.txt", encoding="utf-8", mode="w"
            ) as temp_file:

                temp_file.write(line[i])

        print(text_highlighter("ГОТОВО!"))
        print('\n')
    except:
        print(text_highlighter("КАТАЛОГ ПОКА ЧТО ПУСТ!"))


    
    wanna_cont = input(
                text_highlighter(
                    "Если хотите вернуться в главное меню нажмите 1, завершить программу - любая другая кнопка => "
                ).strip()
            )

    welcome() if wanna_cont == "1" else sys.exit()

# Запуск приложения
welcome()
