# 今天你有三個水果，分別為蘋果，葡萄，香蕉
# 1.請用程式碼加入一個新的水果
# 2.列出現在有幾個水果
# 3.每個水果分別列出：「我手上拿的是XX，好吃！」
# 從以下程式碼開始fruit = ["蘋果","葡萄","香蕉"]
# 在終端機中顯示===>
# 現在水果有4個，分別拿起來吃：）
# 我手上拿的是蘋果，好吃！
# 我手上拿的是葡萄，好吃！
# 我手上拿的是香蕉，好吃！
# 我手上拿的是草莓，好吃！
fruit = ["蘋果","葡萄","香蕉"]
print('現在水果有'+str(len(fruit))+'個，分別拿起來吃：）')

for i in fruit:
  print('我手上拿的是'+i+'，好吃！')

# 1.利用random隨機產生一組數字
# 2.利用if else來判斷<0.1就顯示中獎，
# 其餘顯示沒中獎(中獎機率10%)。
# 3.利用for迴圈連續開三次。
import random

for i in range(0,3,1):
  randomNumber = random.random()
  if randomNumber<0.1:
    print('中獎')
  else:
    print('沒中獎')