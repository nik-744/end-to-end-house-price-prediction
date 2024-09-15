import sys
import os
import pandas as pd
from src.exception import CustomException
from src.utils import load_object

class PredictPipeline:
    def __init__(self) -> None:
        pass

    def predict(self,features):
        try:
            model_path = os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)
        
class CustomData:
    def __init__ (self,
                bedrooms:float,
                bathrooms:float,
                sqft_living:float,
                sqft_lot:float,
                floors:float,
                sqft_above:float,
                sqft_basement:float,
                yr_built:float,
                yr_renovated:float,
                city:str):


                self.bedrooms = bedrooms

                self.bathrooms = bathrooms
                
                self.sqft_living = sqft_living
                
                self.sqft_lot=sqft_lot,
                
                self.floors=floors,
                
                self.sqft_above=sqft_above,
                
                self.sqft_basement =sqft_basement,

                self.yr_built= yr_built,

                self.yr_renovated = yr_renovated,

                self.city = city
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                "bedrooms": [self.bedrooms],
                "bathrooms": [self.bathrooms],
                "sqft_living": [self.sqft_living],
                "sqft_lot": [self.sqft_lot],
                "floors": [self.floors],
                "sqft_above": [self.sqft_above],
                "sqft_basement": [self.sqft_basement],
                "yr_built": [self.yr_built],
                "yr_renovated": [self.yr_renovated],
                "city": [self.city],
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e, sys)
        
