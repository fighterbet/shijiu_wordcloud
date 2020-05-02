# example3.py
# 按图片颜色给文字着色
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread

mk = imread('素材\\belle.png')

# 获取颜色函数
image_colors = ImageColorGenerator(mk)

# 将颜色函数 image_colors 传给 recolor
wc = WordCloud(background_color='white',
               scale=10,
               color_func=image_colors,
               repeat=True,
               mask=mk)

wc.generate('star')
wc.to_file('词云输出\\recolor.png')