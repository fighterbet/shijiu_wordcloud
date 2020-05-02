# example1.py
# 制作图片状词云
from wordcloud import WordCloud

# 导入 imageio 模块的 imread 函数来读取图片内容
from imageio import imread

# 读取图片内容
mk = imread('素材\\五角星.png')

# 设置 mask 参数以获得图片状词云。另外，设置了 repeat 参数使得一个词重复显示以填满图片
wc = WordCloud(background_color='white', repeat=True, mask=mk)

wc.generate('star')
wc.to_file('词云输出\\mask.png')