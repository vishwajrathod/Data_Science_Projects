import numpy as np
import pickle
import json
import config

class BostonHousePrice():
    def __init__(self,CRIM,ZN,INDUS,CHAS,NOX,RM,AGE,DIS,RAD,TAX,PTRATIO,B,LSTAT):
        self.crim = CRIM
        self.zn = ZN
        self.indus = INDUS
        self.chas = CHAS
        self.nox = NOX
        self.rm = RM
        self.age = AGE
        self.dis = DIS
        self.rad = RAD
        self.tax = TAX
        self.ptratio = PTRATIO
        self.b = B
        self.lstat = LSTAT

    def get_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as file:
            self.model = pickle.load(file)
        with open(config.JSON_FILE_PATH,'r') as file:
            self.json_data = json.load(file)

    def get_prediction(self):
        self.get_model()
        test = np.zeros(len(self.json_data['columns']))
        test[0] = self.crim
        test[1] = self.zn
        test[2] = self.indus
        test[3] = self.chas
        test[4] = self.nox
        test[5] = self.rm
        test[6] = self.age
        test[7] = self.dis
        test[8] = self.rad
        test[9] = self.tax
        test[10] = self.ptratio
        test[11] = self.b
        test[12] = self.lstat

        print("Test data is : ",test)

        predicted = self.model.predict([test])
        return predicted