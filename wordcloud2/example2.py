# example2.py
# 勾勒图片轮廓
from wordcloud import WordCloud
from imageio import imread
import matplotlib.pyplot as plt

mk = imread('素材\\belle.png')

# 设置 contour_width 及 contour_width
wc = WordCloud(background_color='white',
               scale=10,
               repeat=True,
               mask=mk,
               contour_width=6,
               contour_color='goldenrod')

wc.generate('star')

# 使用 matplotlib.pyplot 绘制词云和素材的对比图
fig, axes = plt.subplots(1, 2)
axes[0].imshow(wc)
axes[1].imshow(mk)
for ax in axes:
    ax.set_axis_off()

# 保存图片，设置分辨率 dpi=300
plt.savefig('词云输出\\profile.png', dpi=300, bbox_inches='tight')