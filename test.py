# coding=utf-8

from PIL import Image, ImageFilter, ImageFont, ImageDraw
import random


def ramchar():  # 随机生成字母
    return chr(random.randint(65, 90))


def rancolor():  # 颜色是三中颜色组合的，所有需要随机三个
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rancolor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
high = 60
# 新建图像，model是RGB，宽和高，颜色是三种所以都是255
image = Image.new('RGB', (width, high), (255, 255, 255))
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)  # 设置文字的字体
draw = ImageDraw.Draw(image)  # 创建图像
for x in range(width):
    for y in range(high):
        draw.point((x, y), fill=rancolor())  # 对每个像素点进行设置颜色
for t in range(4):  # 输出文字 60*t+10是文字的起始位置，后面的10是字的宽度，高由设置字体的大小决定
    draw.text((60 * t + 10, 10), ramchar(), font = font, fill = rancolor2())
im3 = image.filter(ImageFilter.BLUR)  # 模糊处理
im3.save('yanzhengma.jpg', 'jpeg')


im = Image.open('test.jpg')  # 先打开相应的文件
width,high = im.size  # 读出原来文件的大小
print('Original image size: %s %s' % (width,high))
im.thumbnail((width//2, high//3))  # thumbnail进行大小的调整
print('New image size: %s %s' % (width//2, high//3))
im.save('New.jpg', 'jpeg')  # 保存调整之后的文件
im2 = im.filter(ImageFilter.BLUR)  # 应用过滤器
im2.save('Filted.jpg', 'jpeg')
