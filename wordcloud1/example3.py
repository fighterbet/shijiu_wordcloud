# example3.py
# 制作中文词云
from wordcloud import WordCloud

# 通过 font_path 参数设置支持中文的字体
wc = WordCloud(background_color='white', font_path='SIMLI.TTF')

wc.generate('有的人循规蹈矩，一生碌碌无为，到老之时唉声叹气，责怪命运的不公平；'
            '而有的人，善于创新，关键时放手一搏，即使生命短暂，也活出了不一样的精彩，不一样的闪耀。'
            '命运，永远掌握在自己手中，但要看你是怎样对待它的。')
wc.to_file('词云输出\\chinese.png')