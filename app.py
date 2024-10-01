from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

data = pd.read_csv('Melbourne_housing_FULL.csv')

properties = data.to_dict(orient='records')

@app.route('/')
def index():
    message = 'For properties go to: /api/properties <br> For filtered properties go to: /api/properties/search?suburb=[your_suburb]&min_price=[min_price]&max_price=[max_price]'
    return message


@app.route('/api/properties', methods = ['GET'])
def get_properties():
    return jsonify(properties)


@app.route('/api/properties/search', methods = ['GET'])
def search_properties():
    suburb = request.args.get('Suburb')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)

    filtered_properties = [
        property for property in properties
        if(suburb is None or property['suburb'].lower() == suburb.lower()) and 
        (min_price is None or property['Price'] >= min_price) and
        (max_price is None or property['Price'] <= max_price)
    ]

    return jsonify(filtered_properties)




if __name__ == '__main__':
    app.run(debug=True)