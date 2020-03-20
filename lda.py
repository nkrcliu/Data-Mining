def getText():#get data from thefile
   txt = open(r'C:\\Users\\R.C.Liu\\Desktop\\all reviews.txt', 'r', encoding='ISO-8859-1').read()
   txt = txt.lower()
   for ch in '!"#$%&()*+,-./;:<=>?@[\\]^‘_{|}~':#delete useless symbols
      txt = txt.replace(ch, " ")
   return txt
testTxt = getText()
words = testTxt.split()#devide the sentences into word pieces
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(5000):#out put the most frequent 5000 words in reviews
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))