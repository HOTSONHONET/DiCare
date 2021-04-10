import pickle
from config import *
import numpy as np

class DiCareModel:
    def __init__(self):
        self.model_path = MODEL_PATH
        self.stndscalar_path = STND_SCLR

        self.model = pickle.load(
            open(
                self.model_path,
                'rb'
                )
            )
        
        self.ss = pickle.load(
            open(
                self.stndscalar_path,
                'rb'
                )
            )

    
    def predict(self, data:list) -> dict:
        feats = np.array([data])
        print(f"feats : {feats}")
        print(f"feats dtype : {feats[0]}")
        feats_ss = self.ss.transform(feats)
        neg, pos = self.model.predict_proba(feats_ss)[0]
        verdict = 'Will be readmiited' if pos < 0.5 else 'Healthy'

        response = {
            'healthy' : pos,
            'unhealthy' : neg,
            'verdict' : verdict
        }

        return response



