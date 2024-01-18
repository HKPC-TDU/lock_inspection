from datetime import datetime
from yoloModule import ctrain


class Model:

    def __init__(self, inputs_folder, outputs_folder, history_model_folder):
        self.inputs_folder = inputs_folder
        self.outputs_folder = outputs_folder
        self.history_model_folder = history_model_folder

    def train(self):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'load dataset from {0}'.format(self.inputs_folder))

        # codes of algorithm
    
        print('load parameter from {0}'.format(self.history_model_folder))
        model = self.history_model_folder + 'logs/ep450-loss0.621-val_loss1.252.pth'
        classes = self.history_model_folder + '/classes.txt'
        anchors = self.history_model_folder + 'model_data/yolo_anchors.txt'
        annotation = (self.inputs_folder + '/Annotation/train_label.txt' ,self.inputs_folder + '/Annotation/valid_label.txt')
        output = self.outputs_folder + '/logs'
        # Input para:
        #   a: String => classes path
        #   b: String => anchors path
        #   c: (String, String) => annotation path
        #   d: String => Model path
        #   e: String => Model output path
        print('training')
        ctrain.cpu_eric_train(classes, anchors, annotation, model, output)
        # codes of algorithm

        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 'save model in {0}'.format(self.outputs_folder))
