# example9.py
# 设置“停用词”
from wordcloud import WordCloud
from jieba import lcut

text = '有的人循规蹈矩，一生碌碌无为，到老之时唉声叹气，责怪命运的不公平；' \
       '而有的人，善于创新，关键时放手一搏，即使生命短暂，也活出了不一样的精彩，不一样的闪耀。' \
       '命运，永远掌握在自己手中，但要看你是怎样对待它的。'
text = lcut(text)
text = ' '.join(text)

# stopwords 的词用 大括号 括起来
wc = WordCloud(background_color='white', font_path='SIMLI.TTF', stopwords={'一样', '老之时'})

wc.generate(text)
wc.to_file('词云输出\\stopwords.png')