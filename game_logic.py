"""Реализована игра "крестики-нолики" с партнером"""

field = list(range(1, 10))  # Задаем поле. Список, с числами от 1 до 9


def draw_field(field):
    """
  Функция печати игрового поля
  :param field: принимает для обработки список
  :return: draw_field(field) Печатает поле и текущий ход игрока. Ничего не возвращает.
  """
    print("-" * 13)
    for i in range(3):
        print("|", field[0 + i * 3],
              "|", field[1 + i * 3],
              "|", field[2 + i * 3], "|"
              )
        print("-" * 13)


def take_input(player_token):
    """ Ф-ия ввода данных каждым игроком
        :param player_token: принимает для обработки ввод любого символа
        :return: не возвращает значение, изменяет список
        :except: не int
        Запрашивает ввод, ожидая его int. Обрабатывает исключения - ввод не int.
        Получив ввод int, записывает его в player_answer.
        Проверяет, не является ли элемент списка field под номером (player_answer - 1) строкой, содержащей Х или О.
        Если НЕ является - заменяем элемент списка (player_answer - 1) на символ player_token (Х или О),
        заканчиваем работу функции. Если является - уходим на повторение цикла.
    """

    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token + "? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(field[player_answer - 1]) not in "XO"):
                field[player_answer - 1] = player_token
                valid = True
            else:
                print("Поле уже занято")
        else:
            print("Не вводите 0 (ноль), попробуйте ввести число от 1 до 9.")


def check_win(field):
    """ Ф-ия проверки выигрышных комбинаций

    :param field: принимает список field
    :return: bool

    Получает список поля, проверяет, присутствует ли в нем кортеж из кортежа win_coord
    Если есть - возвращает выигрышный символ Х или О, если нет - False.
    При приведении к bool выигрышный символ дает True.
    """
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if field[each[0]] == field[each[1]] == field[each[2]]:
            return field[each[0]]
    return False


def main(field):
    """ Основная функция.
    :param: принимает список -  поле field
    :return: draw_field(field) Печатает поле и ход игрока. 
    Задаем счетчик ходов, начальное значение 1 (по-человечески)
    Проходим циклом по ф-ии печати игрового поля, заменяя символами Х или О, в зависимости, четный count или нечетный,
    значения в списке field. Увеличиваем count на единицу. Проверяем, что дала ф-ия проверки выигрышных комбинаций.
    Если True - отдаем победу символу, которым заполнен кортеж из win_coord, останавливаем игру.
    Если счетчик ходов принял значение 10, это означает, что ходить больше некуда. Объявляем ничью, останавливаем игру.
    Рисуем поле в текущем цикле.
    Повторяем цикл.
    """
    counter = 1
    win = False
    while not win:
        draw_field(field)
        if counter % 2 == 0:
            take_input("O")
        else:
            take_input("X")
        counter += 1
        if check_win(field):
            print(check_win(field), "победил!")
            win = True
            break
        if counter == 10:
            print("Ничья!")
            break
    draw_field(field)


main(field)




