# Classification Model Training and Quantization

This software is designed for training a convolutional neural network (CNN) based classifier model, particularly for recognizing physical exercises, in the realm of motion tracking. Following the training process, the model undergoes quantization to reduce its memory footprint, ensuring efficient deployment on resource-constrained devices such as wearable trackers or smartphones.

The software is built using PyTorch and takes advantage of PyTorch's quantization utilities.

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [License](#license)

## Features

- **Data preprocessing**: The software includes data downscaling, median filtering, and normalization features.
- **Training a CNN-based model**: The model can be customized with various hyperparameters, including the learning rate, optimizer type, and more.
- **Post-training quantization**: After the training process, the model is quantized using the default QNNPACK backend.
- **Saving the models**: Both the trained and the quantized models are saved for future use.
- **Saving the training parameters and results**: All relevant training parameters and results, such as accuracy and loss, are saved in a JSON file.

## Usage

1. Clone this repository to your local machine.
2. Open the main python script in your preferred Python editor.
3. Set the desired parameters for the training process and the model. These parameters include the learning rate, batch size, epochs, and so on.
4. Run the script using the command `python training.py` in your terminal. This command initiates the training. After training, the model is quantized and saved.
5. The training results will be displayed in the console and also saved in a JSON file within the session path.

## License

This project is licensed under the MIT License.