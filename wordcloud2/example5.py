# example5
# 指定特定词的颜色
# 此段代码修改自文末的官方文档中的示例
from wordcloud import WordCloud, get_single_color_func

# 创建 GroupedColorFunc 类，用于产生颜色函数
class GroupedColorFunc(object):
    def __init__(self, color_to_words, default_color):
        self.color_func_to_words = [
            (get_single_color_func(color), set(words))
            for (color, words) in color_to_words.items()]

        self.default_color_func = get_single_color_func(default_color)

    def get_color_func(self, word):
        """Returns a single_color_func associated with the word"""
        try:
            color_func = next(
                color_func for (color_func, words) in self.color_func_to_words
                if word in words)
        except StopIteration:
            color_func = self.default_color_func

        return color_func

    def __call__(self, word, **kwargs):
        return self.get_color_func(word)(word, **kwargs)

# 从文件中读入文本
with open('素材\\text.txt', 'r') as f:
    text = f.read()
    f.close()

wc = WordCloud(background_color='white', scale=10)
wc.generate(text)

# 创建颜色字典，指定词的颜色。读者可更改颜色、词的列表、添加新颜色、删除颜色等
color_to_words = {
    # 下面列表中的词显示为 orangered 颜色
    'orangered': ['beautiful', 'explicit', 'simple', 'sparse',
                'readability', 'rules', 'practicality',
                'explicitly', 'one', 'now', 'easy', 'obvious', 'better'],
    # 面列表中的词显示为 blue 颜色
    'blue': ['ugly', 'implicit', 'complex', 'complicated', 'nested',
            'dense', 'special', 'errors', 'silently', 'ambiguity',
            'guess', 'hard']
}

# 设置不在字典中的词的颜色
default_color = 'aquamarine'

# 将字典及默认颜色传入以创建 GroupedColorFunc 实例
grouped_color_func = GroupedColorFunc(color_to_words, default_color)

# 将 GroupedColorFunc 实例传入 recolor 方法以按指定规则着色
wc.recolor(color_func=grouped_color_func)

wc.to_file('词云输出\\group.png')