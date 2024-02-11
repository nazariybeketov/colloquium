"""Тестовое задание"""

human_params = [
    "Фамилия",
    "Имя",
    "Отчество",
    "Название организации",
    "Телефон рабочий",
    "Телефон личный (сотовый)",
]


# Добавление пользователя в записную книжку
def add_human(human_params=human_params):

    human = []

    for param in human_params:
        human.append(input(f'Введите поле "{param.upper()}" => '))

    with open(file="catalog.txt", mode="a+", encoding="utf-8") as catalog:

        catalog.seek(0, 2)

        if len(catalog.readlines()) > 0:
            catalog.write("\n")

        catalog.write(" ".join(human))

        print(f"\nКОНТАКТ УСПЕШНО ДОБАВЛЕН!!!\n")


def find_str(counter=0):

    response = []

    ###################

    print("По какому признаку будем искать?\n")
    for i in range(6):
        print(f"{i+1} - {finding_options[i]}")

    print("\n")
    ################### Вывод вариантов ответов

    # Ответ на то, какой вариант поиска нужен
    user_answer = list(
        map(int, input("Введите через пробел вариант/ы поиска => ").split())
    )

    # Словарь для предпочтительных ответов
    desired_answeres = dict()

    # Заполнение словаря
    for temp in user_answer:
        ans = input(f'Введите поле "{finding_options[temp-1]}" => ')
        desired_answeres[finding_options[temp - 1]] = ans

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


######################## Доделать!!!!!!!!!!!!!!!!
def edit_contact():

    lines = find_str()
    if len(lines) > 1:
        print(
            "Под данное описание подходит несколько контактов, если хотите изменить какую-то запись укажите более подробное описание!"
        )
        edit_contact()

    else:
        temp_str = input("Вводите данные: ") + "\n"

        with open(file="catalog.txt", encoding="utf-8", mode="r") as catalog:
            list_of_catalog = catalog.readlines()
            for i in range(len(list_of_catalog)):
                if list_of_catalog[i].strip() == lines[0].strip():
                    list_of_catalog[i] = temp_str
                    break

        with open(file="catalog.txt", encoding="utf-8", mode="w") as catalog:
            catalog.writelines(list_of_catalog)


def page_by_page():
    line = find_str()
    for i in range(len(line)):
        with open(
            file=f"one_record_{i+1}.txt", encoding="utf-8", mode="w"
        ) as temp_file:
            temp_file.write(line[i])


def welcome():
    counter = 0
    print(f"Здравствуйте\n")
    which_cmd = [
        "Вывод постранично записей из справочника на экран",
        "Добавление новой записи в справочник",
        "Редактирования записи в справочнике",
        "Поиск записей по одной или нескольким характеристикам",
    ]

    for i in range(4):
        print(f"{i+1} - {which_cmd[i]}")

    print("\n")
    user_ans = int(input("Какой командой желаете восьпользоваться? => "))

    if user_ans == 1:
        page_by_page()

    elif user_ans == 2:
        add_human()
    elif user_ans == 3:
        edit_contact()

    elif user_ans == 4:
        s = find_str()
        for i in range(len(s)):
            print(s[i])


welcome()
