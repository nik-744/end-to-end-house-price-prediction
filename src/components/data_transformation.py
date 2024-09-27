import sys
from dataclasses import dataclass

import numpy as np 
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"proprocessor.pkl")
    combined_data_file_path=os.path.join("artifacts","combined_data.csv")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_data_transformer_object(self):
        '''
        This function si responsible for data trnasformation
        
        '''
        try:
            categorical_columns=['city']
            numerical_columns=['bedrooms','bathrooms','sqft_living','sqft_lot','floors','sqft_above','sqft_basement','yr_built','yr_renovated']

            num_pipeline= Pipeline(
                steps=[
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())

                ]
            )

            cat_pipeline=Pipeline(

                steps=[
                ("imputer",SimpleImputer(strategy="most_frequent")),
                ("one_hot_encoder",OneHotEncoder(handle_unknown='ignore')),
                ("scaler",StandardScaler(with_mean=False))
                ]

            )

            logging.info(f"Categorical columns: {categorical_columns}")
            logging.info(f"Numerical columns: {numerical_columns}")

            preprocessor=ColumnTransformer(
                [
                ("num_pipeline",num_pipeline,numerical_columns),
                ("cat_pipelines",cat_pipeline,categorical_columns)

                ]


            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_transformation(self,train_path,test_path):

        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="price"
            #numerical_columns = ["writing_score", "reading_score"]

            train_df = train_df.drop(['date','waterfront','view','condition','street','country','statezip'],axis=1)
            test_df = test_df.drop(['date','waterfront','view','condition','street','country','statezip'],axis=1)

            combined_df = pd.concat([train_df,test_df],ignore_index = True)
            combined_df.to_csv(self.data_transformation_config.combined_data_file_path,index=False,header=True)

            logging.info("Data Combined.")

            input_feature_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]

            input_feature_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info(
                f"Applying preprocessing object on training dataframe and testing dataframe."
            )

            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            logging.info("Prepocessing complete.")

            # Convert to dense arrays if they are sparse
            if hasattr(input_feature_train_arr, "toarray"):
                input_feature_train_arr = input_feature_train_arr.toarray()
            
            if hasattr(input_feature_test_arr, "toarray"):
                input_feature_test_arr = input_feature_test_arr.toarray()

            # Converting the shape of target feature of train and test to 2D
            target_feature_train_df = target_feature_train_df.values.reshape(-1, 1)
            target_feature_test_df = target_feature_test_df.values.reshape(-1, 1)

            logging.info("Concatenatiing input features and target features for both train and test datasets")

            train_arr = np.c_[input_feature_train_arr, target_feature_train_df]
            test_arr = np.c_[input_feature_test_arr, target_feature_test_df]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj

            )

            logging.info(f"Saved preprocessing object.")
            return (
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
            )
        except Exception as e:
            raise CustomException(e,sys)