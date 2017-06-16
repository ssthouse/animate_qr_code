from qr_code_generator.main.tools.GifGenerator import GifGenerator

gifGenerator = GifGenerator('https://github.com/ssthouse', src_file='./gif/fox_two.gif', with_bg=False)
imgFileList = ['0.jpg', '1.jpg', '2.jpg', '3.jpg']
# imgList = [Image.open(im) for im in imgFileList]
# gifGenerator.generate_gif_with_imgs(imgFileList, timeSpan=0.3)
gifGenerator.generate_gif_with_gif()
