# крестики-нолики

line_1 = ['-', '-', '-']
line_2 = ['-', '-', '-']
line_3 = ['-', '-', '-']
fields = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
used_fields = []
player = int
i = 0
j = 0

def motion():
    global i, j
    move = str(input("Введите координату:"))
    if move not in fields:
        print("Координата не существует!")
    elif move in used_fields:
        print("Координата занята!")
    else:
        used_fields.append(move)
        if str(move) == '00':
            if player == 1:
                line_1[0] = 'x'
                i += 1
            else:
                line_1[0] = 'o'
                j += 1
        elif str(move) == '01':
            if player == 1:
                line_1[1] = 'x'
                i += 1
            else:
                line_1[1] = 'o'
                j += 1
        elif str(move) == '02':
            if player == 1:
                line_1[2] = 'x'
                i += 1
            else:
                line_1[2] = 'o'
                j += 1
        # line_2
        if str(move) == '10':
            if player == 1:
                line_2[0] = 'x'
                i += 1
            else:
                line_2[0] = 'o'
                j += 1
        elif str(move) == '11':
            if player == 1:
                line_2[1] = 'x'
                i += 1
            else:
                line_2[1] = 'o'
                j += 1
        elif str(move) == '12':
            if player == 1:
                line_2[2] = 'x'
                i += 1
            else:
                line_2[2] = 'o'
                j += 1
        # line_3
        if str(move) == '20':
            if player == 1:
                line_3[0] = 'x'
                i += 1
            else:
                line_3[0] = 'o'
                j += 1
        elif str(move) == '21':
            if player == 1:
                line_3[1] = 'x'
                i += 1
            else:
                line_3[1] = 'o'
                j += 1
        elif str(move) == '22':
            if player == 1:
                line_3[2] = 'x'
                i += 1
            else:
                line_3[2] = 'o'
                j += 1

    print(" ", 0, 1, 2)
    print(0, line_1[0], line_1[1], line_1[2])
    print(1, line_2[0], line_2[1], line_2[2])
    print(2, line_3[0], line_3[1], line_3[2])


def check_win():

    global line_1, line_2, line_3
    if len(used_fields) == 9:
        print('Ничья!')
        main()
    if line_1[0] == line_1[1] == line_1[2] and line_1[0] != '-':
        if line_1[0] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()
    if line_2[0] == line_2[1] == line_2[2] and line_2[0] != '-':
        if line_2[0] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()
    if line_3[0] == line_3[1] == line_3[2] and line_3[0] != '-':
        if line_3[0] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()
    if line_1[0] == line_2[0] == line_3[0] and line_1[0] != '-':
        if line_1[0] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()
    if line_1[1] == line_2[1] == line_3[1] and line_1[1] != '-':
        if line_1[1] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()
    if line_1[2] == line_2[2] == line_3[2] and line_1[2] != '-':
        if line_1[2] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()
    if line_1[0] == line_2[1] == line_3[2] and line_1[0] != '-':
        if line_1[1] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()
    if line_1[2] == line_2[1] == line_3[0] and line_1[2] != '-':
        if line_1[2] == 'x':
            print('Игрок №1 победил!')
            main()
        else:
            print('Игрок №2 победил!')
            main()


def main():

    global used_fields, line_1, line_2, line_3, i, j, player

    i = 0
    j = 0
    line_1 = ['-', '-', '-']
    line_2 = ['-', '-', '-']
    line_3 = ['-', '-', '-']
    used_fields = []

    print(" ", 0, 1, 2)
    print(0, line_1[0], line_1[1], line_1[2])
    print(1, line_2[0], line_2[1], line_2[2])
    print(2, line_3[0], line_3[1], line_3[2])
    print('Введите 2 числа координаты вашего хода по осям x и y, например 01 для хода во вторую клетку первого ряда')

    while True:
        if i == j:
            player = 1
            print('Ходит игрок №', player)
            motion()
            check_win()
        if i > j:
            player = 2
            print('Ходит игрок №', player)
            motion()
            check_win()


if __name__ == "__main__":
    main()
