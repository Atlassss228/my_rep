from random import randint


def index_play(el):
    if count == 0:
        i_last = ""
        i_next = el[count + 1]

    elif count == len(el) - 1:
        i_next = ""
        i_last = el[count - 1]
    else:
        i_next = el[count + 1]
        i_last = el[count - 1]
    return i_next, i_last


def if_consonant(i, slog):
    if i in list_of_consonant:
        if (i in list_of_sonor) and (i_last in list_of_vowel) and (i_next not in list_of_vowel):

            slog += i
            temp = res.pop(-1)
            res.append(temp + slog)
            slog = ""
        else:
            slog += i
            if count == len(el) - 1:
                temp = res.pop(-1)
                res.append(temp + slog)

    return slog


def if_exept(i, slog):
    if i in list_of_exept:
        slog += i
        temp = res.pop(-1)
        res.append(temp + slog)
        slog = ""
    return slog


def if_vowel(i, slog):
    if i in list_of_vowel:
        slog += i
        res.append(slog)
        slog = ""
    return slog


word_list = ["арагорн", "гендзундхайт", "фредерик", "келибримбор",
             "боромир", "аниматрон", "галадриэль", "коромодир", "мефистофель",
             "абелард", "гендальф", "морнингстар",
             "адалбречт",
             "адалвалф",
             "адалрикус",
             "аделбречт",
             "аделхард",
             "амалирикус",
             "ансоберт",
             "бартоломос",
             "виллафрид",
             "гэровалд",
             "джисилберт"
             ]

list_of_vowel = ["а", "и", "е", "о", "у", "ы", "э", "ю", "я"]

list_of_consonant = ["б", "в", "г", "д", "ж", "й", "з", "к", "л", "м",
                     "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]

list_of_sonor = ["р", "л", "м", "н", "й"]

list_of_exept = ["ь", "ъ"]

list_of_rez = []

list_of_middle_slogs = []
list_of_first_slogs = []
list_of_last_slogs = []

for el in word_list:

    res = []
    count = int(0)
    slog = ""
    vowel_mark = False

    for i in el:
        index = index_play(el)
        i_next, i_last = index

        slog = if_consonant(i, slog)

        slog = if_exept(i, slog)

        slog = if_vowel(i, slog)

        count += 1

    list_of_rez.append(res)
    list_of_middle_slogs.extend(res[1:-1])
    list_of_first_slogs.append(res[0])
    list_of_last_slogs.append(res[-1])

middle_list = list_of_middle_slogs
first_list = list_of_first_slogs
last_list = list_of_last_slogs

# print(*list_of_rez)


# print(list_of_last_slogs)
# print(list_of_first_slogs)

# for el in list_of_rez:
#     for i in range(3):
#         final_name = el[0]
#         for z in range(len(el) - 2):
#             final_name += list_of_middle_slogs[randint(0, (len(list_of_middle_slogs) - 1))]
#         final_name += el[-1]
#         print(final_name)
