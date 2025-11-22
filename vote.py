def voting():
    while True:
        try:
            get_age = int(input("Введите ваш возраст: "))
            if get_age < 18:
                print("Вы не можете голосовать!")
                break
            elif get_age >= 18:
                print("Подтверждено!")


                get_citizen = input("Вы являетесь гражданином страны? да/нет: ").lower().strip()
                if get_citizen == "да":
                    print("Потдверждено")
                elif get_citizen == "нет":
                    print("Вы не можете голосовать!")
                    break
                else:
                    print("Введите да или нет!")
                    continue


                get_discualified = input("У вас есть запрет голосовать? да/нет: ").lower().strip()
                if get_discualified == "да":
                    print("Вы не можете голосовать!")
                    break
                elif get_discualified == "нет":
                    print("Подтверждено")
                    print("Поздравляем, вы можете голосовать!")
                    break
                else:
                    print("Введите да или нет!")
                continue
        except ValueError:
            print("Введено не число, введите число!")


voting()


if age() and citizen() and discualified():
    print("Поздравляем, вы сможете проголосовать!")

