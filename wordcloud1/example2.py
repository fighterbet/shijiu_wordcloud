# example2.py
# 改变背景颜色，不再“黑乎乎”
from wordcloud import WordCloud

# 设置背景颜色为白色
wc = WordCloud(background_color='white')

wc.generate('Today you do things people will not do, tomorrow you will do things people can not do.')
wc.to_file('词云输出\\white_background.png')