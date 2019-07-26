class Config(object):
    classes = ["aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow",
               "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train",
               "tvmonitor"]
    default_anchors_path = './data/default_anchors.txt'
    model_save_path = './models/checkpoints/'
    pretrained_model_path = './models/pre_weights/'
    annotation_path = 'data/VOC2007/Annotations/'
    image_path = 'data/VOC2007/Images/'
    label_path = 'data/VOC2007/label_lines.txt'
    output_path = 'data/VOC2007/output/'
    log_dir = 'logs/'
    anchors_path = 'model_data/yolo_anchors.txt'

    input_shape = (416,416)
    batch_size1 = 32
    batch_size2 = 5
    freeze_epoch = 50
    epoch = 100
    lr1 = 1e-3
    lr2 = 1e-4
    val_split = 0.1