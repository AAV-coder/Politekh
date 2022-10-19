# TODO продолжить заполнение словаря
dict_hex = {
    '0x0': 0,
    '0x1': 1,
    '0x2': 2,
}
dict_hex['0x3'] = 3
dict_hex['0x4'] = 4
dict_hex['0x5'] = 5
dict_hex['0x6'] = 6
dict_hex['0x7'] = 7
dict_hex['0x8'] = 8
dict_hex['0x9'] = 9
dict_hex['0xA'] = 10
dict_hex['0xB'] = 11
dict_hex['0xC'] = 12
dict_hex['0xD'] = 13
dict_hex['0xE'] = 14
dict_hex['0xF'] = 15

print(dict_hex)

dict_hex_alternat = {hex(i): i for i in range(16)}
print(dict_hex_alternat)

