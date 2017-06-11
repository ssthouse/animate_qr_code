import time
from MyQR import myqr
import os
import numpy
import imageio
from PIL import Image


class GifGenerator:

    # 默认路径
    BASE_DIR = './temp'
    # 初始二维码文件
    QR_CODE_FILENAME = 'qr_code.png'
    GIF_FILENAME = 'result.gif'

    def __init__(self, url):
        # 初始化传入url
        self.url = url
        # 生成文件夹
        self.tempDir = self.BASE_DIR + '/' + str(int(time.time() * 1000))
        # print(self.tempDir)
        # print(os.getcwd())
        os.mkdir(self.tempDir)
        # 生成二维码文件
        self.generate_qr_code()

    def generate_qr_code(self):
        # 将URL转化为指定名称的二维码文件
        myqr.run(self.url,
                 version=10,
                 level='H',
                 save_name=self._getQrFilePath(),
                 picture='200.jpg',
                 colorized=True)

    def _getQrFilePath(self):
        return self.tempDir + '/' + self.QR_CODE_FILENAME

    def generate_gif_with_imgs(self, imgFileList, timeSpan=0.2):
        imgList = []
        for filename in imgFileList:
            imgList.append(self._get_qr_code_with_img(
                self._getQrFilePath(), imgFileName=filename))
        imgDataList = [numpy.asarray(im, dtype='uint8') for im in imgList]
        imgData = numpy.asarray(imgDataList)
        imageio.mimwrite(self.tempDir + '/' + self.GIF_FILENAME,
                         imgData, duration=timeSpan)

    def generate_gif_with_gif(self, gifFilename, timeSpan=0.2):
        # imgList = imageio.mimread(gifFilename)
        # print(imgList)
        # print(type(imgList[0]))
        gifImg = Image.open(gifFilename)
        imgIndex = 0
        palettee = None
        imgList = []
        while True:
            try:
                gifImg.seek(imgIndex)
                imgList.append(gifImg.copy())
                imgIndex += 1
            except EOFError:
                break
        resizedImgList = [img.resize((200, 200), Image.ANTIALIAS)
                          for img in imgList]
        # 合成图像 => 获得合成的图片列表
        resultImgList = []
        for img in resizedImgList:
            resultImgList.append(self._get_qr_code_with_img(
                self._getQrFilePath(), image=img))
        imgDataList = [numpy.asarray(im, dtype='uint8')
                       for im in resultImgList]
        imgData = numpy.asarray(imgDataList[:7])
        imageio.mimwrite(self.tempDir + '/' + self.GIF_FILENAME,
                         imgData, duration=timeSpan)

    def _get_qr_code_with_img(self, qrFileName, imgFileName=None, image=None):
        # 获取中间的图片Image
        if(imgFileName != None):
            img = Image.open(qrFileName)
        if(image != None):
            img = image
        # 获取嵌入有图片的二维码
        qrImg = Image.open(qrFileName)
        qrImg.paste(img, (200, 200))
        return qrImg
