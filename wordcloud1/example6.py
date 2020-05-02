# example6.py
# 一词成云：repeat 参数
from wordcloud import WordCloud

# 设置 repeat 参数为 True
wc = WordCloud(background_color='white', repeat=True)

wc.generate('star')
wc.to_file('词云输出\\repeat.png')