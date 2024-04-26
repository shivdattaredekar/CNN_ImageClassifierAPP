# Cat and Dog Classifier using VGG16

This project is a simple image classifier built using the VGG16 convolutional neural network architecture to classify images as either cats or dogs.

## APP UI

https://github.com/shivdattaredekar/CNN_ImageClassifierAPP/assets/46707992/b7d0ac2d-3bd4-448b-b2ac-ad9279e190df

## Overview

The classifier is trained on a dataset containing images of cats and dogs. The VGG16 model, pre-trained on the ImageNet dataset, is used as a feature extractor. The final fully connected layers of the VGG16 model are replaced with custom layers to adapt the model for the binary classification task of distinguishing between cats and dogs.

## Requirements

- Python 3.7
- TensorFlow 2.11
- Keras
- numpy
- matplotlib
- Jupyter Notebook (optional, for running and experimenting with the code)

## Installation

Clone the repository:
```
git clone https://github.com/your-username/cat-dog-classifier.git
cd cat-dog-classifier
```

## How to Run

```
1. conda create -n catdog python=3.7 -y
```
```
2. conda activate catdog
```
```
3. pip install -r requirements.txt
```
```
4. python app.py
```


## Project Structure

- `data/`: Contains the dataset of cat and dog images.
- `models/`: Contains the trained model weights.
- `utils/`: Contains utility functions for data preprocessing and image decoding.
- `train.py`: Script for training the classifier.
- `evaluate.py`: Script for evaluating the trained model.
- `predict.py`: Script for making predictions on new images.

## Contributors

- Shivdatta Redekar
- [Gmail](shivdattaredekar@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/shivdatta-redekar-93ab1511a)
- [Upwork](https://www.upwork.com/freelancers/~01860f7d7d31e1cc28)

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/shivdattaredekar/CNN_ImageClassifierAPP/blob/master/LICENSE) file for details.

## Acknowledgements

- The VGG16 model implementation is based on the Keras pre-trained models.


