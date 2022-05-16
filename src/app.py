from flask import Flask, request, send_from_directory
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle

app = Flask(__name__, static_url_path='', static_folder='../client/public')

@app.route('/api/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        try:
            model = load_model('model.h5')

            with open('tokenizer.pickle', 'rb') as handle:
                tokenizer = pickle.load(handle)
            
            if request.json is None:
                return ({ 'message': 'Expected JSON data' }, 400)

            message = request.json.get('message')

            if message is None:
                return ({ 'message': 'Missing field: message' }, 400)

            message = tokenizer.texts_to_sequences([message])

            message = pad_sequences(message, maxlen=100)

            prediction = model.predict(message)

            # Even though the prediction is a 2D numpy array with a shape of (1, 1),
            # checking a condition against a numpy array, will return a new numpy array 
            # where every value has been checked against the condition.

            # [[0.43]] > 0.5 -> [[False]] -> bool([[False]]) -> False
        
            # The resulting array is of the same shape as the original array. And since
            # casting a one-element numpy array to a boolean returns a boolean, it can 
            # be use to check if the prediction is greater than the threshold.
            isSpam = bool(prediction > 0.5)
            
            return { 'isSpam': isSpam }

        except Exception as e:
            print(str(e))

@app.route('/', methods=['get'])
def index():
    return send_from_directory(app.static_folder, 'index.html')
