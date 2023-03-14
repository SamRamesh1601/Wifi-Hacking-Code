
from colorthief import ColorThief
import matplotlib.pyplot as plt
import time 

start = time.time()
image = ColorThief("E:/bg.jpg")

domaint_color = image.get_color(quality=1)

plt.imshow([[domaint_color]])
plt.show()

major_color = image.get_palette(color_count=5)

plt.imshow([[major_color[i] for i in range(5)]])
plt.show()

print(f" domaint color is {domaint_color}")
print(f" Color is {major_color}")
end = time.time()

print(f" seconds take over this program is {(end-start)/60} s ")
