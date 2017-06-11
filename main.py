from tools.GifGenerator import GifGenerator
import imageio
from PIL import Image

gifGenerator = GifGenerator('https://baidu.com')
imgFileList = ['0.jpg', '1.jpg', '2.jpg', '3.jpg']
# imgList = [Image.open(im) for im in imgFileList]
# gifGenerator.generate_gif_with_imgs(imgFileList, timeSpan=0.3)
gifGenerator.generate_gif_with_gif('new.gif', timeSpan=0.02)
