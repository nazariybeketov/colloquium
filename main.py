"""

Тестовое задание

"""

from typing import NoReturn
from lists import human_params, which_cmd


# Главное меню
def welcome(which_cmd: list[str] = which_cmd) -> NoReturn:
    counter = 0
    print(f"Здравствуйте\n")

    for i in range(5):
        print(f"{i+1} - {which_cmd[i]}")

    print("\n")
    user_ans = int(input("Какой командой желаете восьпользоваться? => "))

    match user_ans:
        case 1:
            page_by_page()

        case 2:
            add_human()
        case 3:
            edit_contact()

        case 4:
            s = find_human()
            for i in range(len(s)):
                print(s[i])
            welcome()
        case 5:
            ...
        case _:
            print("Такой команды не существует :9")


# Функция добавления пользователя
def add_human(human_params: list[str] = human_params) -> str:

    human = []

    for param in human_params:
        human.append(input(f'Введите поле "{param.upper()}" => '))

    with open(file="catalog.txt", mode="a+", encoding="utf-8") as catalog:

        catalog.seek(0, 2)

        if len(catalog.readlines()) > 0:
            catalog.write("\n")

        catalog.write(" ".join(human))

        print(f"\nКОНТАКТ УСПЕШНО ДОБАВЛЕН!!!\n")


# Функция поиска человека
def find_human(
    response: list[str] = [],
    counter: int = 0,
    finding_options: list[str] = human_params,
) -> list[str]:

    ################### Вывод вариантов ответов

    print("По какому признаку будем искать?\n")
    for i in range(6):
        print(f"{i+1} - {finding_options[i]}")

    print("\n")
    ###################

    # Ответ на то, какой вариант/ы поиска нужен/ы
    user_answer = list(
        map(int, input("Введите через пробел вариант/ы поиска => ").split())
    )

    # Словарь для предпочтительных ответов
    desired_answeres = dict()

    # Заполнение словаря
    for k in user_answer:
        ans = input(f'Введите поле "{finding_options[k-1]}" => ')
        desired_answeres[finding_options[k - 1]] = ans

    # Работа с файлом
    with open(file="catalog.txt", encoding="utf-8", mode="r") as catalog:
        #####
        for line in catalog.readlines():
            elements_of_working_line = line.split()
            ##### Рабочая строка

            for answer in user_answer:
                if (
                    elements_of_working_line[answer - 1]
                    == desired_answeres[finding_options[answer - 1]]
                ):
                    counter += 1
            if counter == len(user_answer):
                counter = 0
                response.append(line)
    return response


# Функция редактирования контакта
def edit_contact(human_params: list[str] = human_params) -> NoReturn:

    line = find_human()

    if len(line) == 1:
        print(f"Что хотите изменить?\n")
        for i in range(len(human_params)):
            print(f"{i} - {human_params[i]}")
        print("\n")

        user_answer = list(
            map(
                int,
                input("Введите через пробел поля, которые нужно заменить => ").split(),
            )
        )
        new_line = line[0].split()
        for j in user_answer:
            new_line[j] = input(f'Введите поле "{human_params[j]}" => ')

        new_line = " ".join(new_line) + "\n"

        with open(file="catalog.txt", encoding="utf-8", mode="r") as catalog:
            list_of_catalog = catalog.readlines()
            for i in range(len(list_of_catalog)):
                if list_of_catalog[i].strip() == line[0].strip():
                    list_of_catalog[i] = new_line
                    break

        with open(file="catalog.txt", encoding="utf-8", mode="w") as catalog:
            catalog.writelines(list_of_catalog)
            wanna_cont = int(
                input(
                    "Если хотитет внести еще изменения нажмите 1, вернуться в главное меню - 2"
                )
            )
            edit_contact() if wanna_cont == 1 else welcome()
    elif len(line) > 1:
        print(
            "Под данное описание подходит несколько контактов, если хотите изменить какую-то запись укажите более подробное описание!"
        )
        edit_contact()

    else:
        print(f"Ни одной записи не нашлось :(\n")
        print(f"Попробуйте найти с другими параметрами!\n")
        edit_contact()


# Функция постраничного вывода контактов
def page_by_page() -> NoReturn:
    line = find_human()
    for i in range(len(line)):
        with open(
            file=f"one_record_{i+1}.txt", encoding="utf-8", mode="w"
        ) as temp_file:
            temp_file.write(line[i])


# Запуск приложения
welcome()
