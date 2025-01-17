# тема "Многопроцессное программирование"
# Задача "Многопроцессное считывание"

from multiprocessing import Pool
from datetime import datetime

def read_info(name):
    all_data=[]
    with open(name, 'r') as f:
        while line := f.readline():
            all_data.append(line.strip())

files_list = [f'file {i}.txt' for i in range(1,5)]

# Линейный вызов

# start_time = datetime.now()
# for i in range(len(files_list)):
#     read_info(files_list[i])
# end_time = datetime.now()
# execution_time = end_time - start_time
# print(execution_time, 'Линейный вызов')

# Многопроцессный вызов

if __name__ == '__main__':
    start_time = datetime.now()
    with Pool() as pool:
        pool.map(read_info, files_list)
        end_time = datetime.now()
    execution_time = end_time - start_time
    print(execution_time, 'Многопроцесный вызов')

# END
