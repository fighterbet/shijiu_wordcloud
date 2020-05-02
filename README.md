# python词云从入门到精通
以下 「python词云基本用法」 的代码及素材包含在 wordcloud1 文件夹中，「python词云高手进阶」 的代码及素材包含在 wordcloud2 文件夹中。

## python词云模块的安装
制作词云的主要模块为 `wordcloud`，另外，要使用 `jieba` 库切割中文句子，用 `imageio` 读入图片。在命令行中执行以下命令即可安装：
```
pip install wordcloud jieba imageio
```

## python词云基本用法
### 制作你的第一个词云
下面用四行代码制作了一个词云，代码中包含了详细的注释：

```python
# example1.py
# 从词云模块 wordcloud 导入 WordCloud 类
from wordcloud import WordCloud

# 创建一个 WordCloud 对象 wc
wc = WordCloud()

# 将字符串传入 wc 对象的 generate 方法（此时只能处理英文）
wc.generate('Today you do things people will not do, tomorrow you will do things people can not do.')

# 利用 to_file 方法将词云输出到指定路径
wc.to_file(r'词云输出\first_wordcloud.png')
```
![first_wordcloud](https://upload-images.jianshu.io/upload_images/23208742-813399db699688df.png?imageMogr2/auto-orient/strip|imageView2/2/w/400/format/webp)

### 改变背景颜色，不再“黑乎乎”
上面制作的词云的显得黑乎乎的，不好看，此时需要更改词云的背景颜色。

只要简单改变上述创建 WordCloud 对象的代码，即可得到不同背景颜色的词云：
```python
# example2.py
# 设置背景颜色为白色
wc = WordCloud(background_color='white')
```
![white_background](https://upload-images.jianshu.io/upload_images/23208742-ec5beb4c08477637.png?imageMogr2/auto-orient/strip|imageView2/2/w/400/format/webp)

python还支持很多颜色，下表列出了一部分，有兴趣的读者可自行尝试：

|单词|颜色|
|:-:|:-:|
|gray|灰色||coral|珊瑚色||magenta|洋红色|
|lightcoral|浅珊瑚色||brown|棕色||fuchsia|紫红色|
|firebrick|火砖色||red|红色||darkorchid|暗紫色|
|orangered|橘红色||goldenrod|金麒麟色||blueviolet|蓝紫色|
|greenyellow|黄绿色||chartreuse|黄绿色||dodgerblue|闪蓝色|
|lawngreen|草坪绿||aquamarine|碧绿色||deepskyblue|深天蓝色|
|turquoise|蓝绿色||cyan|蓝绿色||red|红色|

### 制作中文词云
可能有的读者已经发现，上面的代码使用中文字符串时，输出的词云会显示一堆大小不一的方框，看不到中文的影子。

原因在于 WordCloud 使用的默认字体没有为中文编码，所以没办法显示中文。

要显示中文同样很简单，只需在创建 WordCloud 对象时通过设置 `font_path` 参数设置支持中文的字体即可：

```python
# example3.py
# 通过 font_path 参数设置支持中文的字体
wc = WordCloud(background_color='white', font_path='SIMLI.TTF')
```

其中，字体的名称 SIMLI.TTF 表示隶书，如果读者电脑有这种字体，就能正常显示中文了。
![chinese](https://upload-images.jianshu.io/upload_images/23208742-df2b2896c2707523.png?imageMogr2/auto-orient/strip|imageView2/2/w/400/format/webp)

另外，Windows 系统可以在 C:\Windows\Fonts 路径下找到能使用的字体，通过 查看 -> 选择详细信息 -> 勾选字体文件名称 的操作，显示字体文件名称，然后就可以如图所示地找到字体对应的英文名称了。

![查看字体名称](https://upload-images.jianshu.io/upload_images/23208742-b883408aac598374.png?imageMogr2/auto-orient/strip|imageView2/2/w/1156/format/webp)

### 把中文句子“切开”

上面制作的中文词云，中文是整句整句显示的，不是我们想要的一个一个的词。

要制作由一个一个词组成的词云，就要借助 `jieba` 库把句子切割成词：

```python
# example4.py
# 从 jieba 模块导入切割句子的函数 lcut
from jieba import lcut

text = '永远掌握在自己手中'

# 将句子切开
text = lcut(text)
print(text)
```

运行后得到如下结果：

> ['永远', '掌握', '在', '自己', '手中']

### 中文分词词云
话不多说，先上代码：

```python
# example5
from wordcloud import WordCloud
from jieba import lcut

text = '有的人循规蹈矩，一生碌碌无为，到老之时唉声叹气，责怪命运的不公平；' \
       '而有的人，善于创新，关键时放手一搏，即使生命短暂，也活出了不一样的精彩，不一样的闪耀。' \
       '命运，永远掌握在自己手中，但要看你是怎样对待它的。'
text = lcut(text)

# 利用空格将分散的中文词练成一个单独的字符串，注意引号内有一个空格
text = ' '.join(text)

wc = WordCloud(background_color='white', font_path='SIMLI.TTF')
wc.generate(text)
wc.to_file('词云输出\\partition.png')
```
![partition](https://upload-images.jianshu.io/upload_images/23208742-f71a4f2152804250.png?imageMogr2/auto-orient/strip|imageView2/2/w/400/format/webp)

值得注意的是，利用 `jieba` 切割句子后，得到的是多个词组成的列表，但 WordCloud 的 generate 方法要求传入一个单独的字符串，所以要把单词用空格连成一个字符串。

连词成串用到 `join` 方法，注意上面代码的引号中有一个空格。

### 一词成云：repeat 参数
用一个单词做词云，只需在创建 WordCloud 对象时设置 `repeat` 参数为 `True`：

```python
# example6.py
from wordcloud import WordCloud

# 设置 repeat 参数为 True
wc = WordCloud(background_color='white', repeat=True)

wc.generate('star')
wc.to_file('词云输出\\repeat.png')
```
![repeat](https://upload-images.jianshu.io/upload_images/23208742-483549c54bf1e451.png?imageMogr2/auto-orient/strip|imageView2/2/w/400/format/webp)

### 单一颜色的词云
制作单一颜色的词云，需要在创建 WordCloud 对象时设置 color_func 函数。读者只需更改下面代码的颜色即可体验其他颜色：

```python
# example7.py
from wordcloud import WordCloud

# 设置 color_func 函数， 读者只需修改最后的颜色即可
wc = WordCloud(background_color='white', repeat=True, color_func=lambda *args, **kwargs: "deepskyblue")

wc.generate('star')
wc.to_file('词云输出\\singlecolor.png')
```
![singlecolor](https://upload-images.jianshu.io/upload_images/23208742-71174999e84f71b6.png?imageMogr2/auto-orient/strip|imageView2/2/w/400/format/webp)

### 制作高清词云：scale 参数
细心的朋友可能已经发现，前面制作的词云清晰度普遍较低，如何制作高清词云呢？

其实只需将 `scale` 参数设置成更大的值（默认值为 1）：

```python
# example8.py
from wordcloud import WordCloud

# 将 scale 参数设置为 10
wc = WordCloud(background_color='white', repeat=True, scale=10)

wc.generate('star')
wc.to_file('词云输出\\highdefinition.png')
```
![hith_definition](https://upload-images.jianshu.io/upload_images/23208742-cb135c024fd141f6.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

### 设置“停用词”
停用词用于指定词云不显示哪些词，在代码中将 `stopwords={'词1', '词2', ...}` 传入 WordCloud 类即可：

```python
# example9.py
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
```
![stopwords](https://upload-images.jianshu.io/upload_images/23208742-16e536e18a8a5af5.png?imageMogr2/auto-orient/strip|imageView2/2/w/400/format/webp)

### WordCloud 类参数小结
通过传入不同参数到 `wc = WordCloud()` ，我们可以轻松获得不同属性的词云：

|参数|说明|
|:-:|:-|
|width|输出图片的宽度，要求整型数|
|height|输出图片的高度，要求整型数|
|background_color|背景颜色|
|font_path|字体类型，制作中文词云时要用支持中文的字体|
|repeat|布尔类型，在输入词很少时可以重复显示以填满图片，默认不重复|
|scale|浮点数，越大，输出的图片越清晰，默认为1|
|stopwords|设置不显示的词，用大括号括起来|

## python词云高手进阶
### 制作图片状词云
关键点在于利用
- 利用 `imageio.imread()` 读入图片内容
- 设置 WordCloud 的 `mask` 参数

```python
# example1.py
from wordcloud import WordCloud

# 导入 imageio 模块的 imread 函数来读取图片内容
from imageio import imread

# 读取图片内容
mk = imread('素材\\五角星.png')

# 设置 mask 参数以获得图片状词云。另外，设置了 repeat 参数使得一个词重复显示以填满图片
wc = WordCloud(background_color='white', repeat=True, mask=mk)

wc.generate('star')
wc.to_file('词云输出\\mask.png')
```
![mask](https://upload-images.jianshu.io/upload_images/23208742-bf1ceb3dfafee930.png?imageMogr2/auto-orient/strip|imageView2/2/w/500/format/webp)

值得注意的是，如果图片背景不是白色或者透明，则依然会有文字填充。

### 勾勒图片轮廓
勾勒图片轮廓只需通过 `contour_width` 参数设置轮廓线宽度，`contour_color` 参数设置轮廓线颜色。

```python
# example2.py
from wordcloud import WordCloud
from imageio import imread
import matplotlib.pyplot as plt

mk = imread('素材\\belle.png')

# 设置 contour_width 及 contour_width
wc = WordCloud(background_color='white',
               scale=10,
               repeat=True,
               mask=mk,
               contour_width=6,
               contour_color='goldenrod')

wc.generate('star')

# 使用 matplotlib.pyplot 绘制词云和素材的对比图
fig, axes = plt.subplots(1, 2)
axes[0].imshow(wc)
axes[1].imshow(mk)
for ax in axes:
    ax.set_axis_off()

# 保存图片，设置分辨率 dpi=300
plt.savefig('词云输出\\profile.png', dpi=300, bbox_inches='tight')
```
![profile](https://upload-images.jianshu.io/upload_images/23208742-8ee8876a3bb4b038.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

### 按图片颜色给文字着色
需要先将图片传入 `ImageColorGenerator` 类，获取返回的颜色函数，再将此函数传入 WordCloud 的 `recolor` 属性：

```python
# example3.py
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread

mk = imread('素材\\belle.png')

# 获取颜色函数
image_colors = ImageColorGenerator(mk)

# 将颜色函数 image_colors 传给 recolor
wc = WordCloud(background_color='white',
               scale=10,
               color_func=image_colors,
               repeat=True,
               mask=mk)

wc.generate('star')
wc.to_file('词云输出\\recolor.png')
```
![recolor](https://upload-images.jianshu.io/upload_images/23208742-f9d19eabc6471ed0.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

下面的例子用于对比用图片颜色着色与默认着色效果。在创建 WordCloud 对象时，没有传颜色函数给 `color_func`，而是在后面调用 WordCloud 对象的 `recolor()` 方法传入颜色函数：

```python
# example4.py
from wordcloud import WordCloud, ImageColorGenerator
from imageio import imread
import matplotlib.pyplot as plt

mk = imread('素材\\belle.png')
wc = WordCloud(background_color='white',
               scale=20,
               repeat=True,
               mask=mk)
wc.generate('star')

# 利用 ImageColorGenerator 类生成颜色函数
image_colors = ImageColorGenerator(mk)

fig, axes = plt.subplots(1, 3)

# 显示使用默认着色方案的词云
axes[0].imshow(wc, interpolation="bilinear")

# 用 WordCloud 的 recolor 方法根据图片颜色重新给文字上色
axes[1].imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")

# 显示原图片
axes[2].imshow(mk, cmap=plt.cm.gray, interpolation="bilinear")
for ax in axes:
    ax.set_axis_off()

plt.savefig('词云输出\\recolor2.png', dpi=300, bbox_inches='tight')
```
![recolor2](https://upload-images.jianshu.io/upload_images/23208742-7dbe3eff86486d85.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

### 指定特定词的颜色
下面代码中，构建了 GroupedColorFunc 类，利用该类产生颜色函数。

构建了一个 color_to_words 字典，键名为颜色，键值是显示为该颜色的词的列表。读者只需修改此字典即可更改词的颜色。

将字典及默认颜色传入 GroupedColorFunc 类创建该类的实例，再将此实例传入 WordCloud 对象的 `recolor` 方法即可。

```python
# example5
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
```
![group](https://upload-images.jianshu.io/upload_images/23208742-b4150e82bd881d95.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

**至此，你已经是python词云能手了，快去创作自己的词云吧！**

## 参考资料
- 官方文档:「[WordCloud for Python documentation](http://amueller.github.io/word_cloud/index.html)」
- b站:「[词云可视化：四行Python代码轻松上手到精通](https://www.bilibili.com/video/BV1i4411W76Z?p=1)」
- github:「[amueller/word_cloud](https://github.com/amueller/word_cloud)」
