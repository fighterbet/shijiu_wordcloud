# example1.py
# 制作你的第一个词云
# 从词云模块 wordcloud 导入 WordCloud 类
from wordcloud import WordCloud

# 创建一个 WordCloud 对象 wc
wc = WordCloud()

# 将字符串传入 wc 对象的 generate 方法（此时只能处理英文）
wc.generate('Today you do things people will not do, tomorrow you will do things people can not do.')

# 利用 to_file 方法将词云输出到指定路径
wc.to_file(r'词云输出\first_wordcloud.png')