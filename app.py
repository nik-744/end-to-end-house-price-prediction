from flask import Flask , render_template,request
import pandas as pd
from src.pipeline.predict_pipeline import CustomData , PredictPipeline
from src.pipeline.recommendation_pipeline import recommendation

house_data = pd.read_csv(r'artifacts\combined_data.csv')  # Load your house dataset
# house_data.dropna(inplace=True)
recommender = recommendation(house_data)  # Create a recommendation instance


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods=['POST','GET'])
def predictdata():
    if request.method == 'GET':
        return render_template('predict.html',results=None,recommendations=None)
    else:
        data = CustomData(
        bedrooms = request.form.get('bedrooms'),
        bathrooms = request.form.get('bathrooms'),
        sqft_living = request.form.get('sqft_living'),
        sqft_lot = request.form.get('sqft_lot'),
        floors = request.form.get('floors'),
        sqft_above = request.form.get('sqft_above'),
        sqft_basement = request.form.get('sqft_basement'),
        yr_built = request.form.get('yr_build'),
        yr_renovated = request.form.get('yr_renovated'),
        city = request.form.get('city')
        )

        images = [
                "https://images.pexels.com/photos/106399/pexels-photo-106399.jpeg?auto=compress&cs=tinysrgb&w=800",
                  "https://images.pexels.com/photos/1396122/pexels-photo-1396122.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
                  "https://images.pexels.com/photos/164558/pexels-photo-164558.jpeg?auto=compress&cs=tinysrgb&w=800",
                  "https://images.pexels.com/photos/1396132/pexels-photo-1396132.jpeg?auto=compress&cs=tinysrgb&w=800",
                  "https://images.pexels.com/photos/280222/pexels-photo-280222.jpeg?auto=compress&cs=tinysrgb&w=800",
                  "https://images.pexels.com/photos/259588/pexels-photo-259588.jpeg?auto=compress&cs=tinysrgb&w=800"
                  ]
        # print(images)
        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline=PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)

        similar_houses = recommender.recommend_similar_houses(results[0],pred_df)
        # print(similar_houses)
        # print(similar_houses.shape)
        # print(type(similar_houses))
        is_empty = similar_houses.empty if similar_houses is not None else True

        
        return render_template('predict.html',
                                results=results[0],
                                similar_houses=similar_houses,
                                is_empty = is_empty,
                                images=images
                               )
        

if __name__=="__main__":
    app.run(debug=True)

