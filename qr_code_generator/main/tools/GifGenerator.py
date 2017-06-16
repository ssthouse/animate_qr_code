import time
from MyQR import myqr
import os
import numpy
import imageio
from PIL import Image


class GifGenerator:
    # 默认路径
    BASE_DIR = 'static/temp'
    # 初始二维码文件
    QR_CODE_FILENAME = 'qr_code.png'
    # 动图的一些常量数据
    GIF_FILENAME = 'result.gif'
    QR_CODE_WIDTH = 477
    GIF_PAST_POINT = (163, 163)
    GIF_SIZE = (150, 150)

    def __init__(self, url, src_file, with_bg=False):
        self.gif_duration = 0.02
        # 初始化传入url
        self.url = url
        self.src_file = src_file
        self.with_bg = with_bg
        self.tempDir = self.BASE_DIR + '/' + str(int(time.time() * 1000))
        os.mkdir(self.tempDir)
        # 生成二维码文件
        self.generate_qr_code()

    def generate_qr_code(self):
        # 将URL转化为指定名称的二维码文件
        bg_file = './static/200.jpg'
        if self.with_bg:
            # 将gif第一张图保存下来
            gif_img = Image.open(self.src_file)
            bg_file = self.tempDir + '/' + 'bg.png'
            gif_img.save(bg_file)
        myqr.run(self.url,
                 version=7,
                 level='H',
                 save_name=self._get_qr_file_path(),
                 picture=bg_file,
                 colorized=True)

    def _get_qr_file_path(self):
        return self.tempDir + '/' + self.QR_CODE_FILENAME

    def get_result_path(self):
        return self.tempDir + '/' + self.GIF_FILENAME

    def generate_gif_with_imgs(self, imgFileList, timeSpan=0.2):
        imgList = []
        for filename in imgFileList:
            imgList.append(self._get_qr_code_with_img(
                self._get_qr_file_path(), imgFileName=filename))
        imgDataList = [numpy.asarray(im, dtype='uint8') for im in imgList]
        imgData = numpy.asarray(imgDataList)
        imageio.mimwrite(self.tempDir + '/' + self.GIF_FILENAME,
                         imgData, duration=timeSpan)

    def generate_gif_with_gif(self):
        gifImg = Image.open(self.src_file)
        # 初始化动图间隔
        self.gif_duration = gifImg.info['duration'] / 1000.0
        imgList = self._get_imgs_from_gif(gifImg)
        resizedImgList = [img.resize(self.GIF_SIZE, Image.ANTIALIAS)
                          for img in imgList]
        # 合成图像 => 获得合成的图片列表
        resultImgList = []
        for img in resizedImgList:
            resultImgList.append(self._get_qr_code_with_img(
                self._get_qr_file_path(), image=img))
        imgDataList = [numpy.asarray(im, dtype='uint8')
                       for im in resultImgList]
        imgData = numpy.asarray(imgDataList)
        imageio.mimwrite(self.tempDir + '/' + self.GIF_FILENAME,
                         imgData, duration=self.gif_duration)

    def _get_imgs_from_gif(self, gif_img):
        # 获取动图的图片序列
        imgIndex = 0
        imgList = []
        while True:
            try:
                gif_img.seek(imgIndex)
                imgList.append(gif_img.copy())
                imgIndex += 1
            except EOFError:
                break
        return imgList

    def _get_qr_code_with_img(self, qrFileName, imgFileName=None, image=None):
        # 获取带有中间的图片Image
        if (imgFileName != None):
            img = Image.open(qrFileName)
        if (image != None):
            img = image
        # 获取嵌入有图片的二维码
        qrImg = Image.open(qrFileName)
        qrImg.paste(img, self.GIF_PAST_POINT)
        return qrImg
