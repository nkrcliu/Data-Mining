from wordcloud import WordCloud
import numpy as np
import jieba

def trans_CN(text):
    word_list = jieba.cut(text)
    # 分词后在单独个体之间加上空格
    result = " ".join(word_list)
    return result;


with open("C:\\Users\\R.C.Liu\\Desktop\\Matthew O. Jackson - Social and Economic Networks-Princeton University Press (2008) (1)(1)\\lunwen.txt",encoding='utf-8') as fp:
    text = fp.read()
    text  = trans_CN(text)
    # print(text)
    #mask = np.array(image.open("F:\\20180612151652413.png"))
    wordcloud = WordCloud(background_color="white",
        font_path = "C:\\Windows\\Fonts\\msyh.ttc"
    ).generate(text)
    image_produce = wordcloud.to_image()
    image_produce.show()