def get_count_char(str_):
    result_str_ = str_.lower().strip()
    symbol_amount = dict((letter, result_str_.count(letter)) for letter in set(result_str_))

    return symbol_amount

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))
print(len(main_str))
