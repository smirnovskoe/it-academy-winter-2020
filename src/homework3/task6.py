""" Task 6: Упорядоченный список
Дан список целых чисел. Требуется переместить все ненулевые элементы в левую
часть списка, не меняя их порядок, а все нули - в правую часть. Порядок
ненулевых элементов изменять нельзя, дополнительный список использовать
нельзя, задачу нужно выполнить за один проход по списку.
Распечатайте полученный список.
"""


def order_list(_list=None):
    """


    :param _list:
    :return: None
    """
    last_idx = 0
    for idx, element in enumerate(_list):
        if not element:
            continue
        _list[last_idx], _list[idx] = _list[idx], _list[last_idx]
        last_idx += 1

    print(_list)


if __name__ == "__main__":
    lst = [0, -1, 0, 1, 0, 0, 3, 5, 0, 7, 13, 0]
    order_list(lst)