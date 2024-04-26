from flask import Flask, request, jsonify, render_template
import os
from com_in_ineuron_ai_utils.utils import decodeImage
from prediction.predict import DogCat

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = DogCat(self.filename)


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predictRoute():
    image = request.json['image']
    decodeImage(image, clApp.filename)
    result = clApp.classifier.predictiondogcat()
    return jsonify(result)


if __name__ == "__main__":
    clApp = ClientApp()
    app.run(port=5000)
