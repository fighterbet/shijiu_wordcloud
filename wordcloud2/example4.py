# example4.py
# 对比用图片颜色着色与默认着色效果
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread
import matplotlib.pyplot as plt

mk = imread('素材\\belle.png')
wc = WordCloud(background_color='white',
               scale=20,
               repeat=True,
               mask=mk)
wc.generate('star')

# 利用 ImageColorGenerator 类生成颜色函数
image_colors = ImageColorGenerator(mk)

fig, axes = plt.subplots(1, 3)
axes[0].imshow(wc, interpolation="bilinear")

# 用 WordCloud 的 recolor 方法根据图片颜色重新给文字上色
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")

axes[2].imshow(mk, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()

plt.savefig('词云输出\\recolor2.png', dpi=300, bbox_inches='tight')