import numpy as np
import json
import pickle
import config


class Diabetes():
    def __init__(self,age,sex,bmi,bp,s1,s2,s3,s4,s5,s6):
        self.age = age
        self.sex = sex
        self.bmi = bmi
        self.bp  = bp
        self.s1  = s1
        self.s2  = s2
        self.s3  = s3
        self.s4  = s4
        self.s5  = s5
        self.s6  = s6
    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as file:
            self.model = pickle.load(file)
        with open(config.JSON_FILE_PATH,'r') as file:
            self.json_data = json.load(file)
    def get_predicted_diabetes(self):
        self.load_model()
        test_array = np.zeros(len(self.json_data["columns"]))
        test_array[0] = self.age
        test_array[1] = self.sex
        test_array[2] = self.bmi
        test_array[3] = self.bp
        test_array[4] = self.s1
        test_array[5] = self.s2
        test_array[6] = self.s3
        test_array[7] = self.s4
        test_array[8] = self.s5
        test_array[9] = self.s6
        print("Test array is : ",test_array)

        predicted_diabetes = self.model.predict([test_array])
        return predicted_diabetes
