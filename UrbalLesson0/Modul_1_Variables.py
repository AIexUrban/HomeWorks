homeworks_completed = 12
hours = 1.5
cource_name = 'Python'
one_task_time = hours / homeworks_completed

print('Курс: ', cource_name, ', ',  'всего задач: ', homeworks_completed, ', '+
      'затрачено часов: ', hours, ','+ ' среднее время выполнения: ', one_task_time, ' часа'+
      ', то есть - ', one_task_time*60, ' мин.', sep='')
print(f'Курс: {cource_name}, всего задач: {homeworks_completed}, затрачено часов: {hours},'
      f' среднее время выполнения: {one_task_time} часа, то есть - {one_task_time*60} мин.')

# END
