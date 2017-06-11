from tools.save_pic_2_gif import generate_qr_code, get_qr_code_with_img, save_pics_2_gif

base_dir = './temp'


def generate_qr_code_with_imgs():
    # 1.生成二维码文件
    qr_code_filename = base_dir + '/qr_code.png'
    generate_qr_code('https://baidu.com', qr_code_filename)
    # 2.获取带有嵌入图片的二维码
    fileList = ['0.jpg', '1.jpg', '2.jpg', '3.jpg']
    imgList = []
    for file_name in fileList:
        qrImg = get_qr_code_with_img(qr_code_filename, imgFileName=file_name)
        imgList.append(qrImg)
    # 3.保存生成的图片序列到gif文件
    save_pics_2_gif(imgList=imgList, gifName=base_dir + '/please.gif')


generate_qr_code_with_imgs()
