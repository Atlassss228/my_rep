import pickle
import json
from name_creator import middle_list, first_list, last_list
from random import randint

def add_acc(account_dict, command_args):
    # add номер_счета имя_человека золото
    text = "Хранилище создано, Повелитель!"
    if 999999 >= int(command_args[0]) >= 99999:
        account_dict[int(command_args[0])] = [command_args[1], int(command_args[2])]
    else:
        text = "Недостаточно суровый номера хранилища, Повелитель! "

    return text


def close_acc(account_dict, command_args):
    req_acc = int(command_args[0])
    # close номер_счета
    text = "Нет такого номера среди номеров хранилищь, Повелитель!"
    if req_acc in account_dict:
        account_dict.pop(req_acc)
        text = f"Хранилище {req_acc} сожжено успешно, Повелитель! До тла!!! В пепел!!!!!"
    return text


def put_gold(account_dict, command_args):
    # put номер_счета золото
    req_acc = int(command_args[0])
    text = "Нет такого номера среди номеров хранилищь, Повелитель!"
    if req_acc in account_dict:
        add = int(command_args[1])
        account_dict[req_acc][1] += add
        text = f"Принято {add} золота, Повелитель! Но ведь все равно мало да?"
    return text


def take_gold(account_dict, command_args):
    # take номер_счета золото
    req_acc = int(command_args[0])
    text = "Нет такого номера среди номеров хранилищ, Повелитель!"
    if req_acc in account_dict:
        add = int(command_args[1])
        if account_dict[req_acc][1] < add:
            add = account_dict[req_acc][1]
        account_dict[req_acc][1] -= add
        text = f"От сердца оторвано и возвращено {add} золота, Пвелитель! Кругом Враги..."
    return text


def trans_gold(account_dict, command_args):
    # trans номер_счета1 номер_счета2 золото_переводимое
    req_acc1 = int(command_args[0])
    req_acc2 = int(command_args[1])

    text = "Лютая хрень с номерами хранилищь, Повелитель!"
    if req_acc1 in account_dict and req_acc2 in account_dict:
        add = int(command_args[2])
        if account_dict[req_acc1][1] < add:
            add = account_dict[req_acc1][1]
        text = f"Из хранилича {req_acc1} в хранилище {req_acc2} перевезено {add} золота!"
        account_dict[req_acc1][1] -= add
        account_dict[req_acc2][1] += add
    return text


def print_acc_dict(account_dict, command_args):
    for el in account_dict:
        print(f"{el} {account_dict[el][0]} : {account_dict[el][1]}")
    text = "Конец ведомости по хранилищам, Повелитель!"
    return text


def exit(account_dict, command_args):
    text = "Выхожу из сумрака"
    return text


def export_to_json(account_dict, command_args):
    text = "Ведомость экспортирована и записана в джесон, Повелитель!"
    with open("baseinf.json", "wt") as f:
        json.dump(account_dict, f)
    return text


def import_from_json(account_dict, command_args):
    text = "Ведомость импортирована из джесона, Повелитель!"
    with open("baseinf.json", "rt") as f:
        account_dict = json.load(f)
    return text


def basesave(account_dict, command_args):
    text = "Ведомость сохранена, Повелитель!"
    with open("baseinf.pickle", "wb") as f:
        pickle.dump(account_dict, f)
    return text

def autoadd(account_dict, command_args):
    # autoadd количество счетов, комбинация имени( AA BBB CC), сумма золота
    text = f"Список из {command_args[0]} жалких червей создан, Повелитель!"

    for el in range(int(command_args[0])):
        acc_num = randint(100000, 999999)
        acc_value = command_args[2]
        acc_name = ""
        for i in command_args[1]:
            if i == "A":
                acc_name += first_list[randint(0, len(first_list)-1)]
            elif i == "B":
                acc_name += middle_list[randint(0, len(middle_list)-1)]
            elif i == "C":
                acc_name += last_list[randint(0, len(last_list)-1)]

        account_dict[acc_num] = [acc_name, int(acc_value)]

    return text

def command_pars(data):
    command_list = data.split()
    return command_list[0], command_list[1:]
