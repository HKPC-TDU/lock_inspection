from yoloModule import predict as p
import os

class ModelPredict:

    def __init__(self, inputs_folder, outputs_folder, model_folder):
        self.inputs_folder = inputs_folder
        self.outputs_folder = outputs_folder
        self.model_folder = model_folder

    def predict(self):
        print('load input from {0}'.format(self.inputs_folder))

        # codes of algorithm
        print('predict')
        img_path = self.inputs_folder
        out_path = self.outputs_folder
        img_list = os.listdir(img_path)

        #p.set_input_path(self.model_folder)
        for img in img_list:
            p.new_pred(img_path+"/"+img, out_path+img)
        # codes of algorithm

        print('save result in {0}'.format(self.outputs_folder))
