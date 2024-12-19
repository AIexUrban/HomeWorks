# Записать и запомнить

def custom_write(file_name, string):
    string_positions = {}
    with open(file_name, 'w', encoding='utf-8') as f:
        j = 0
        for i in string:
            j += 1
            bite_nom_str_pos = (j, f.tell())
            f.write(f'{i}\n')
            string_positions[bite_nom_str_pos] = i
    return string_positions

info = ['Text for tell.',
        'Используйте кодировку utf-8.',
        'Because there are 2 languages!',
        'Спасибо!']

result = custom_write('test.txt', info)

for elem in result.items():
        print(elem)

# END
