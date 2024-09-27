# House Price Prediction
## Overview
This project predicts house prices based on various features like the number of bedrooms, bathrooms, square footage, year built, and more. It also recommends similar houses from a dataset based on the predicted price. The project is built using Flask for the web application, Pandas for data processing, and Scikit-Learn for model predictions.

## Features
- Predict house prices based on features such as:
  - Number of bedrooms
  - Number of bathrooms
  - Square footage of living area and lot
  - Number of floors
  - Year built and year renovated
  - City
- Recommend similar houses based on the predicted price.
- Display images for the recommended houses.
- Responsive and interactive frontend.
## Tech Stack
- Backend: Flask (Python)
- Machine Learning: Scikit-Learn
- Data Processing: Pandas
- Frontend: HTML, CSS (with Flexbox for responsive design), Jinja2 templating
- Dataset: House data loaded from a CSV file

Project Structure

```graphql

├── app.py               # Main Flask application
├── src
|   ├── components
|   |   ├── data_ingestion.py # Code for loading the dataset
|   |   ├── data_transformation.py # Code for making necessary transformations
|   |   ├── model_trainer.py # Code for training the model
│   ├── pipeline
│   │   ├── predict_pipeline.py  # Code for making predictions
│   │   ├── recommendation_pipeline.py  # Code for recommending similar houses
├── static
│   ├── style.css        # CSS for the frontend
├── templates
│   ├── index.html       # Home page
│   ├── predict.html     # House price prediction page
├── artifacts
│   ├── combined_data.csv # Dataset for house prices
├── README.md            # Project documentation
```
## Setup Instructions
### Prerequisites
- Python 3.x
- Flask
- Pandas
- Scikit-Learn
- A dataset for house prices (combined_data.csv)

# Installation
* Clone the repository:

```bash
git clone https://github.com/nik-744/end-to-end-house-price-prediction.git
```
* Navigate to the project directory:

```bash
cd house-price-prediction
```
* Install the required packages:

```bash
pip install -r requirements.txt
```
* Add your dataset in the artifacts folder. Ensure it is named combined_data.csv.

Running the Application
Run the Flask app:

```bash
python app.py
```
Open your browser and go to http://127.0.0.1:5000/.

## Making Predictions
Fill in the form with house details like bedrooms, bathrooms, etc.
Click on the "Predict House Price" button to see the predicted price.
If similar houses are found, they will be listed along with their images.
Dataset
The dataset (combined_data.csv) contains information about houses, including:

- Price
- Number of bedrooms and bathrooms
- Square footage of living area, lot, and basement
- Year built and renovated
- City
  
You can update this dataset with new data or preprocess it to remove any missing or irrelevant values.
To do that, make sure you edit the values in the `data_ingestion.py` , `data_transformation.py`, `model_trainer.py` and modify `pridict.html` according to your dataset features.

## Models
The house price prediction model is built using Scikit-Learn's regression models. A recommendation system is also in place, which compares the predicted price with other houses in the dataset and suggests similar ones.

## Frontend Design
The form to input house details is built using HTML and styled with CSS, following a two-column layout for better usability. Recommended houses are displayed with their corresponding images, price, and other features.

## Issues and Contributions
If you encounter any issues, feel free to submit them in the Issues section. Contributions are welcome!
