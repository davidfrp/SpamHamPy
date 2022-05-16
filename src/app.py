from flask import Flask, request
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model
import pickle

app = Flask(__name__)

@app.route('/', methods=['post'])
def predict():
    try:
        model = load_model('SpamHam.h5')

        with open('tokenizer.pickle', 'rb') as handle:
            tokenizer = pickle.load(handle)

        message = request.json.get('message')

        message = tokenizer.texts_to_sequences([message])

        message = pad_sequences(message, maxlen=100)

        prediction = model.predict(message)[0][0]

        isSpam = bool(prediction > 0.5)
        
        return { 'isSpam': isSpam }

    except Exception as e:
        print(str(e))

# if __name__ == '__main__':
#     app.run()