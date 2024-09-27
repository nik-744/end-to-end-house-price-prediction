import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

class recommendation:
    def __init__(self, house_data):
        """
        Initialize the Recommendation system with the existing house dataset.
        
        house_data: A pandas DataFrame containing house features like price, bedrooms, location, etc.
        """
        self.house_data = house_data
        
        # Define the features to use for the recommendation
        self.features = ['price', 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated']
        
        # Handle missing values using SimpleImputer
        self.imputer = SimpleImputer(strategy='mean')  # Replace NaNs with the mean of each column
        self.house_data[self.features] = self.imputer.fit_transform(self.house_data[self.features])

        # Ensure there are no NaN values after imputation
        if self.house_data[self.features].isnull().values.any():
            raise ValueError("There are still NaN values in the data after imputation")

        # Scale the features to make KNN distance calculation fairer
        self.scaler = StandardScaler()
        self.scaled_data = self.scaler.fit_transform(self.house_data[self.features])
        
        # Initialize and fit the KNN model on the house data
        self.knn_model = NearestNeighbors(n_neighbors=5, algorithm='auto')
        self.knn_model.fit(self.scaled_data)
    
    def recommend_similar_houses(self, predicted_price, input_data):
        """
        Recommend similar houses based on the predicted price and other house features.
        
        predicted_price: The house price predicted by the model.
        input_data: The data of the input house used for the prediction.
        n_recommendations: The number of similar houses to recommend.
        
        Returns a DataFrame of recommended houses.
        """
        n_recommendations = 6
        
        # Add the predicted price to the input data
        input_data['price'] = predicted_price
        
        # Handle missing values in input_data (using the same strategy as in training data)
        input_data[self.features] = self.imputer.transform(input_data[self.features])

        # Ensure there are no NaN values in the input data after imputation
        if input_data[self.features].isnull().values.any():
            raise ValueError("There are still NaN values in the input data after imputation")

        # Select only the relevant features and scale them
        input_features = input_data[self.features]
        scaled_input = self.scaler.transform(input_features)
        
        # Find similar houses using the KNN model
        distances, indices = self.knn_model.kneighbors(scaled_input, n_neighbors=n_recommendations)
        
        # Get the recommended houses from the dataset
        recommended_houses = self.house_data.iloc[indices[0]]
        
        return recommended_houses
