# example8.py
# 制作高清词云：scale 参数
from wordcloud import WordCloud

# 将 scale 参数设置为 10
wc = WordCloud(background_color='white', repeat=True, scale=10)

wc.generate('star')
wc.to_file('词云输出\\highdefinition.png')