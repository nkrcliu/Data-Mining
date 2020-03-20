import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
sales = pd.read_csv("C:\\Users\\R.C.Liu\\Desktop\\第2周数据集：1-sale.csv", encoding='ISO-8859-1')
x = range(1, 202)
y = sales["amount"].values
plt.plot(x, y, alpha=0.6)
plt.title('Time series of sale')
plt.show()
errorvalue = []
for i in y:
    if i > 4000:
        errorvalue.append(i)
    elif i < 1500:
        errorvalue.append(i)
for j in errorvalue:
    sales.loc[sales['amount'] == j ] = None
sales['amount'].fillna(sales['amount'].mean(), inplace=True)
print(sales)
sales.to_csv('D:\\sales_new.csv')
