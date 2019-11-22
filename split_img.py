import cv2
import os

# 将一张图片按大小从左上、左下、右上、右下切分为四张图像
class Split_img():

    # 输入:要切割的图片，要切割成的长和宽
    def __init__(self, img_path, split_height, split_weight):
        super().__init__()

        self.img_name = str(img_path).split('/')[-1]
        self.img_path = str(img_path).replace(self.img_name, '')
        self.img_type = str(img_path).split('.')[-1]

        self.img = cv2.imread(img_path)

        self.split_height = split_height
        self.split_weight = split_weight

        self.img_height = self.img.shape[0]
        self.img_weight = self.img.shape[1]

        assert self.split_height <= self.img_height and self.split_weight <=self.img_weight

    def split(self):
        print(self.img_name)
        print(self.img_path)
        print(self.img_type)

        img1 = self.img[0:self.split_height, 0:self.split_weight]
        img2 = self.img[(self.img_height-self.split_height):self.img_height, 0:self.split_weight]
        img3 = self.img[0:self.split_height, (self.img_weight-self.split_weight):self.img_weight]
        img4 = self.img[(self.img_height-self.split_height):self.img_height, (self.img_weight-self.split_weight):self.img_weight]

        print(self.img_weight - (self.img_weight - self.split_weight))
        print(self.img.shape)
        print(self.img_height)
        print(self.img_weight)
        print(img1.shape)
        print(img2.shape)
        print(img3.shape)
        print(img4.shape)

        save_path = os.path.join(self.img_path, 'split_imgs')
        if not os.path.exists(save_path):
            os.makedirs(save_path)

        cv2.imwrite(os.path.join(save_path, 'img1.'+self.img_type), img1)
        cv2.imwrite(os.path.join(save_path, 'img2.'+self.img_type), img2)
        cv2.imwrite(os.path.join(save_path, 'img3.'+self.img_type), img3)
        cv2.imwrite(os.path.join(save_path, 'img4.'+self.img_type), img4)

split_img = Split_img('a.png', 1000, 1000)
split_img.split()

