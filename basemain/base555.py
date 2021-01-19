from myfunc import *
import pickle

with open("baseinf.pickle", "rb") as f:
    account_dict = pickle.load(f)

command_dict = {"add": add_acc, "print": print_acc_dict, "close": close_acc,
                "put": put_gold, "take": take_gold, "trans": trans_gold,
                "export": export_to_json, "import": import_from_json,
                "exit": exit, "autoadd": autoadd}

text = ""

while text != "Выхожу из сумрака":
    case = input("Введите повеление: /add /close /put /take /print /trans /exit "
                 "/import /export /autoadd\n")
    command, command_args = command_pars(case)

    if command in command_dict:
        text = command_dict[command](account_dict, command_args)

        print(text + "\n")
        basesave(account_dict, command_args)

    else:
        print("Лютая хрень с повелениями, о Повелитель!")
