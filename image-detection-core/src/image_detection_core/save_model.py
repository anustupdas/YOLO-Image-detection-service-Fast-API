import tensorflow as tf
from image_detection_core.yolo.yolov4 import YOLO, decode, filter_boxes
import image_detection_core.yolo.utils as utils
from image_detection_core.constants import *
from image_service_foundation.config.configuration_manager import ConfigurationManager

class Model_Converter:
  def __init__(self, config: ConfigurationManager):
    self.config = config
    self.weights = self.config.get('yolo.weightPath', DEFAULT_YOLO_DOWNLOAD_WEIGHT_PATH)
    self.output = self.config.get('yolo.finalweights', DEFAULT_YOLO_FINAL_WEIGHT_PATH)
    self.tiny = self.config.get('yolo.tiny', DEFAULT_YOLO_TINY)
    self.input_size = self.config.get('yolo.input_size', DEFAULT_YOLO_INPUT_SIZE)
    self.score_thres = self.config.get('yolo.score_threshold', DEFAULT_YOLO_SCORE_THRESHOLD)
    self.framework = self.config.get('yolo.framework', DEFAULT_YOLO_FRAMEWORK)
    self.model = self.config.get('yolo.model', DEFAULT_YOLO_MODEL_NAME)

  def save_tf(self):
    STRIDES, ANCHORS, NUM_CLASS, XYSCALE = utils.load_config(self)

    input_layer = tf.keras.layers.Input([self.input_size, self.input_size, 3])
    feature_maps = YOLO(input_layer, NUM_CLASS, self.model, self.tiny)
    bbox_tensors = []
    prob_tensors = []
    if self.tiny:
      for i, fm in enumerate(feature_maps):
        if i == 0:
          output_tensors = decode(fm, self.input_size // 16, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, self.framework)
        else:
          output_tensors = decode(fm, self.input_size // 32, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, self.framework)
        bbox_tensors.append(output_tensors[0])
        prob_tensors.append(output_tensors[1])
    else:
      for i, fm in enumerate(feature_maps):
        if i == 0:
          output_tensors = decode(fm, self.input_size // 8, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, self.framework)
        elif i == 1:
          output_tensors = decode(fm, self.input_size // 16, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, self.framework)
        else:
          output_tensors = decode(fm, self.input_size // 32, NUM_CLASS, STRIDES, ANCHORS, i, XYSCALE, self.framework)
        bbox_tensors.append(output_tensors[0])
        prob_tensors.append(output_tensors[1])
    pred_bbox = tf.concat(bbox_tensors, axis=1)
    pred_prob = tf.concat(prob_tensors, axis=1)
    if self.framework == 'tflite':
      pred = (pred_bbox, pred_prob)
    else:
      boxes, pred_conf = filter_boxes(pred_bbox, pred_prob, score_threshold=self.score_thres, input_shape=tf.constant([self.input_size, self.input_size]))
      pred = tf.concat([boxes, pred_conf], axis=-1)
    model = tf.keras.Model(input_layer, pred)
    utils.load_weights(model, self.weights, self.model, self.tiny)
    model.summary()
    model.save(self.output)
