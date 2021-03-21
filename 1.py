import requests

import time
a = int(input('爬取张数:'))
b=1
while b <= a:
  time.sleep(3)    #设置延时秒数
  print('正在爬取第%d张'%b)
  img_url = 'https://api.dongmanxingkong.com/suijitupian/acg/1080p/index.php'  #填写要爬取的图片api
  response=requests.get(img_url)

  with open('img/%d.jpg'%b,'wb') as f:     #存储到img路径下
       f.write(response.content)
  print('第%d张爬取成功'%b)
  b=b+1
print('爬取完成')
