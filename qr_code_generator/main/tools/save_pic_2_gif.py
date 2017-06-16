# coding=utf-8

from PIL import Image, ImageDraw
import numpy
import imageio
from MyQR import myqr

def save_pics_2_gif(imgList, gifName='test.gif', duration=0.2):
    # resize the image to 200*200
    #resized_list = [im.resize((200, 200), Image.ANTIALIAS) for im in imgList]
    # convert image to nparray
    resized_list = [numpy.asarray(im, dtype='uint8') for im in imgList]
    # save image list to gif
    pic_frames = numpy.asarray(resized_list)
    imageio.mimwrite(gifName, pic_frames, duration=duration)


# save_pics_2_gif(['1.jpg', '2.jpg'], gifName='teset_func.gif')


def generate_qr_code(url, fileName):
    # 将URL转化为指定名称的二维码文件
    myqr.run(url,
             version=10,
             level='H',
             save_name=fileName,
             picture='200.jpg',
             colorized=True)


generate_qr_code('https://baidu.com', 'func.gif')


def get_qr_code_with_img(qrFileName, imgFileName):
    # 获取嵌入有图片的二维码
    qrImg = Image.open(qrFileName)
    img = Image.open(imgFileName)
    qrImg.paste(img, (200, 200))
    return qrImg


def get_sized_pic(imgFileName, size=(200, 200)):
    # 将图片转换为指定的大小
    # get_sized_pic('1.jpg')
    img = Image.open(imgFileName)
    return img.resize(size, Image.ANTIALIAS)
