def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()  # При вызове функции inner_function внутри фцнкции test_function\
                      # печати не происходит

test_function()  # при вызове test_function печать производится, так как inner_function\
                 # находится в локальном пространстве test_function.
inner_function()  # А привызове вне функции test_function происходит ошибка,
                  # так как функция не определена в глобальном пространстве.



