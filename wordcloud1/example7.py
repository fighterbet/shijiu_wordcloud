# example7.py
# 单一颜色的词云
from wordcloud import WordCloud

# 设置 color_func 函数， 读者只需修改最后的颜色即可
wc = WordCloud(background_color='white', repeat=True, color_func=lambda *args, **kwargs: "deepskyblue")

wc.generate('star')
wc.to_file('词云输出\\singlecolor.png')