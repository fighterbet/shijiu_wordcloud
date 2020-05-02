# example4.py
# 把中文句子“切开”
# 从 jieba 模块导入切割句子的函数 lcut
from jieba import lcut

text = '永远掌握在自己手中'

# 将句子切开
text = lcut(text)
print(text)