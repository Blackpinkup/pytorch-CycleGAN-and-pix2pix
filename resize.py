import os
import cv2
from tqdm import tqdm


if __name__ == '__main__':
    # root_dir = 'E:/DeepLearning/GAN/pytorch-CycleGAN-and-pix2pix-master/datasets'
    # dataset = 'vegetable'
    #data_dir = os.path.join(root_dir, dataset, 'images')
    #sdata_dir = os.path.join(root_dir, dataset, 'simages')
    data_dir = 'E:/DeepLearning/GAN/pytorch-CycleGAN-and-pix2pix-master/datasets/server'
    sdata_dir = 'E:/DeepLearning/GAN/pytorch-CycleGAN-and-pix2pix-master/datasets/server2'
    # if os.path.exists(sdata_dir) == False:
    #     os.mkdir(sdata_dir)
    img_list = os.listdir(data_dir)
    for img_name in tqdm(img_list):
        img_pth = os.path.join(data_dir, img_name)
        img = cv2.imread(img_pth)
        #new_img_pth = os.path.join(sdata_dir, img_name)
        #new_img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)), interpolation=cv2.INTER_CUBIC)
        new_img = cv2.GaussianBlur(img, (19, 19), 0)
        #cv2.imwrite(new_img_pth, new_img)
        new_img_pth = os.path.join(sdata_dir, img_name)
        cv2.imwrite(new_img_pth, new_img)
    