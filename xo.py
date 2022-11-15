def print_map(p):
    print(' ', *list(range(len(p))))
    for idx, i in enumerate(p):
        print(idx, *i)


def get_move_coord(p):
    try:
        coord = list(
            map(int, input(f'ходит "{p.upper()}"|введите "x" и "y":').split()))
    except ValueError:
        print('Неверные данные, введите числа в диапазоне от 0 до 2. Пример "0 0", "0 2"\n')
        get_move_coord(p)

    if all([0 <= x <= 2 for x in coord]):
        return coord

    print('Неверные данные, введите числа в диапазоне от 0 до 2. Пример "0 0", "0 2"\n')
    get_move_coord(p)


def check_win(d):
    win_position = [[1, 2, 3], [1, 5, 9], [1, 4, 7], [
        2, 5, 8], [3, 6, 9], [4, 5, 6], [7, 8, 9], [3, 5, 7]]

    for i in d:
        for j in win_position:
            if list(set(d[i]) & set(j)) == j:
                return True


def get_player():
    x, o = 'x', 'o'
    while True:
        x, o = o, x
        yield o


def run_game():
    map_ = [['#', '#', '#'], ['#', '#', '#'], ['#', '#', '#']]

    players_position = {
        "x": [],
        "o": []
    }

    print_map(map_)

    for i in get_player():
        print(f'Ход игрока "{i.upper()}"')
        coord = get_move_coord(i)

        while True:
            if map_[coord[0]][coord[1]] == '#':
                map_[coord[0]][coord[1]] = i
                players_position[i] = sorted(
                    players_position[i] + [coord[0]*3 + coord[1] + 1])
                break
            else:
                print('Поле занато, выберите друго поле')
                coord = get_move_coord(i)

        if check_win(players_position):
            print(f'Игрок {i.upper()} победил')

            break

        print_map(map_)
        print('*'*30)


if __name__ == "__main__":
    run_game()
