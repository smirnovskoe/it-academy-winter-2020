""" Task 3: Tuple practice
- Создайте список ['a', 'b', 'c'] и сделайте из него кортеж.
- Создайте кортеж ('a', 'b', 'c'), И сделайте из него список
- Сделайте следующие присвоения одной строкой a = 'a', b=2, c=’python’.
- Создайте кортеж из одного элемента, чтобы при итерировании по этому
  элементы последовательно выводились значения 1, 2, 3.
  Убедитесь что len() исходного кортежа возвращает 1.
"""


if __name__ == "__main__":
    # step 1
    _list = ['a', 'b', 'c']
    _tuple = tuple(_list)

    # step 2
    _tpl = ('a', 'b', 'c')
    _lst = list(_tpl)

    # step 3
    a, b, c = 'a', 2, 'python'

    # step 4 ???????????????????????????????
    tuple_ = '123',

    for element in tuple_:
        print(list(element))

    print(len(tuple_))
