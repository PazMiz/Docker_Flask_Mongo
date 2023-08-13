from flask import Flask, jsonify, request
from pymongo import MongoClient
import certifi
from bson import ObjectId  # Import ObjectId
from flask_cors import CORS  # Import the CORS extension
from flask_pymongo import PyMongo

app = Flask(__name__)
CORS(app)

# MongoDB configuration
MONGO_URI = "mongodb+srv://PazM:paz053239@cluster0.dqw0io7.mongodb.net/Flask_Crud"  # Replace with your MongoDB Atlas connection string
DB_NAME = 'Flask_Crud'

# Initialize MongoClient with SSL certificate options
client = MongoClient(MONGO_URI, tls=True, tlsCAFile=certifi.where())

# Access the 'Flask_Crud' database
db = client[DB_NAME]

# Sample route to add a single car to the "cars" collection
@app.route('/add_cars', methods=['POST'])
def add_car():
    car_data = request.json  # Get the car data from the request body

    # Convert ObjectId to string
    car_data['_id'] = str(ObjectId())

    # Insert the car data into the 'cars' collection
    db.cars.insert_one(car_data)
    return jsonify(car_data)

# Sample route to retrieve all cars from the MongoDB collection
@app.route('/cars', methods=['GET'])
def get_all_cars():
    cars = list(db.cars.find({}, {'_id': 0}))  # Retrieve all cars from the 'cars' collection
    return jsonify(cars)

@app.route('/delete_car/<string:car_id>', methods=['DELETE'])
def delete_car(car_id):
    db.cars.delete_one({'_id': ObjectId(car_id)})
    return "Car deleted from the 'cars' collection."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
