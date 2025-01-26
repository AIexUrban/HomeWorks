# Использование библиотеки matplotlib

# Построение круговой диаграммы

import matplotlib.pyplot as plt
import numpy as np
from time import sleep

plt.style.use('_mpl-gallery-nogrid')


# Задаем параметры диаграммы
x = [4, 2, 3, 7, 3, 5]
colors = plt.get_cmap('Blues')(np.linspace(0.9, 0.1, len(x)))

# Задаем вид диаграммы
fig, ax = plt.subplots()
ax.pie(x, colors=colors, radius=3, center=(4, 4),
       wedgeprops={"linewidth": 0.5, "edgecolor": "white"}, frame=True)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()

sleep(5)

# ------------------------------------------
# Использование библиотеки pillow


from PIL import Image, ImageDraw, ImageFont
img = Image.open('test_pic.jpg')
rotated = img.rotate(180)
rotated.save('rotated_test_pic.jpg')
img = Image.open('rotated_test_pic.jpg')
img.show()
sleep(3)

# Уменьшаем размер изображения
img = Image.open('rotated_test_pic.jpg')
img = img.resize((800, 500))
img.save('rotated_test_pic_resize.jpg')
img = Image.open('rotated_test_pic_resize.jpg')
img.show()
sleep(3)

# Переворачиваем обратно уменьшенное изображение
# Выводим текст на изображении

img = Image.open('rotated_test_pic_resize.jpg')
rotated = img.rotate(180)
rotated.save('rotated_test_pic_rotate.jpg')
img = Image.open('rotated_test_pic_rotate.jpg')
font = ImageFont.truetype("arial.ttf", size=45)
idraw = ImageDraw.Draw(img)
idraw.text((25, 25), 'Использование библиотеки Pillow', font=font)
img.save('test_text.jpg')
img = Image.open('test_text.jpg')
img.show()
