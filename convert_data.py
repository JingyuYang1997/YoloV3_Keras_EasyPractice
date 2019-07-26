import xml.etree.ElementTree as ET
import glob
from config import Config

cfg = Config()
classes = cfg.classes
annotation_path = cfg.annotation_path
label_path = cfg.label_path

def convert_annotation(annotation_id, label_file):
    in_file = open(annotation_path+'{}.xml'.format(annotation_id))
    tree=ET.parse(in_file)
    root = tree.getroot()
    label_file.write(annotation_id+'.jpg')
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
        label_file.write('\t'+",".join([str(a) for a in b]) + ',' + str(cls_id))
    label_file.write('\n')
    in_file.close()


image_lists = glob.glob(cfg.image_path+'*jpg')
label_file = open(label_path, 'w')
for image_name in image_lists:
    annotation_id = image_name.split('\\')[-1].split('.')[0]
    convert_annotation(annotation_id, label_file)
label_file.close()

