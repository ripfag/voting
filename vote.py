def age():
    while True:
        try:
            get_age = int(input("Введите ваш возраст:"))
            break
        except ValueError:
            print("Введено не число, введите число!")
            return


    if get_age < 18:
        print("Вы не можете голосовать!")
        return False
    elif get_age >= 18:
        print("подтверждено")
        return True


def citizen():
    while True:
        try:
            get_citizen = str(input("Вы являетесь гражданином страны?(да/нет)")).strip().lower()
        except ValueError:
            print ("Введите да или нет!")
        except TypeError:
            print("Введите да или нет!")


        if get_citizen == "да":
            print("подтверждено")
            return True
        elif get_citizen == "нет":
            print("Вы не можете голосовать!")
            return False
        else:
            print("Введите да или нет!")


def discualified():
    while True:
        try:
            get_discualified = str(input("У вас есть запрет голосовать? (да/нет)")).strip().lower()
        except TypeError:
            print("Введите да или нет!")


        if get_discualified == "да":
            print("Вы не можете голосовать!")
            return False
        elif get_discualified == "нет":
            print("Вы можете голосовать!")
            return True
        else:
            print("Введите да или нет!")


if age() and citizen() and discualified():
    print("Поздравляем, вы сможете проголосовать!")
