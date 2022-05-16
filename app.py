from flask import Flask, render_template, request
from tensorflow.keras.models import load_model

app = Flask(__name__)

@app.route('/',methods=['post','get'])
def predict():
    try:
        model = load_model('yogamodel.h5')

# with open('tokenizer.pickle', 'rb') as handle:
#     tokenizer = pickle.load(handle)

    except Exception as e:
        print(str(e))
        # return render_template('index.html', result= str(e))

if __name__ == '__main__':
    app.run()