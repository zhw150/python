import requests
import time
import datetime;
import random;

a = int(input('爬取张数:'))
b=1
while b <= a:
 for i in range (0,1):
  nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S");#生成当前时间
  randomNum=random.randint(0,100);#生成的随机整数n，其中0<=n<=100
  if randomNum<=10:
    randomNum=str(0)+str(randomNum);
  uniqueNum=str(nowTime)+str(randomNum);
  c=int(uniqueNum)

  time.sleep(3)    #设置延时秒数
  print('正在爬取第%d张'%b)
  img_url = 'https://api.dongmanxingkong.com/suijitupian/acg/1080p/index.php'  #填写要爬取的图片api
  response=requests.get(img_url)

  with open('img/%d.jpg'%c,'wb') as f:     #存储到img路径下
       f.write(response.content)
  print('第%d张爬取成功'%b)
  b=b+1
print('爬取完成')
