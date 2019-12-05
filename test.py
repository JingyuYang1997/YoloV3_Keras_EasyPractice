import sys
import argparse
from yolo_detect import YoloDetect, detect_video
from PIL import Image
from config import Config
import glob
import os

cfg = Config()
if not os.path.exists(cfg.output_path):
    os.mkdir(cfg.output_path)

def detect_img(yolo):
    images = glob.glob(cfg.image_path+'*.jpg')
    for img in images:
        img_id = img.split('\\')[-1].split('.')[0]
        try:
            image = Image.open(img)
        except:
            print('Open Error! Try again!')
            continue
        else:
            r_image = yolo.detect_image(image)
            r_image.save(cfg.output_path+img_id+'_op.jpg')
            # r_image.show()
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--model_path', type=str,
        help='path to model weight file, default ' + YoloDetect.get_defaults("model_path"),
		default= cfg.model_save_path+'trained_weights_final.h5')
    FLAGS = parser.parse_args()
    detect_img(YoloDetect(**vars(FLAGS)))
