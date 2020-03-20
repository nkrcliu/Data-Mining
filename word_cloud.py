from wordcloud import WordCloud


def getText():
   txt = open(r'C:\\Users\\R.C.Liu\\Desktop\\C题：文本情感分析代码\\Textming\\negdes.txt', 'r', encoding='ISO-8859-1').read()
   txt = txt.lower()
   for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':
      txt = txt.replace(ch, " ")
   return txt

f = getText()
wordcloud = WordCloud(background_color="white",
                      width=1000, height=860, margin=2,
                      stopwords={'baby','one','daughter','in','the','and','of','my','son','this','is','but','br','from','to','just','are','all','it','so','was','that','which','or','it','on','with','when','because','also'}).generate(f)
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
plt.axis("off")
plt.show()