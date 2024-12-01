# Подсчет суммы всего, что есть в первоначальном списке

data_structure = [
[1, 2, 3, '234'],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_sum(data_structure):
    total=0
    if isinstance(data_structure, (int, float)):
        total += data_structure
    elif isinstance(data_structure, str):
        total += len(data_structure)
    elif isinstance(data_structure, (list, tuple,set)):
        for item in data_structure:
            total += calculate_sum(item)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            total += calculate_sum(key)
            total += calculate_sum(value)
    return total

result = calculate_sum(data_structure)
print(result)


