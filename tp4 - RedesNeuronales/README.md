# Trabajo Práctico 4 - Redes Neuronales

## Problem: Traffic Sign Recognition

### Introduction

As advancements in autonomous vehicle development progress, a key challenge lies in computer vision. This allows cars to comprehend their surroundings through digital images. In particular, it involves the ability to recognize and distinguish traffic signals such as stop signs, speed limits, yield signs, and more.

In this project, TensorFlow will be used to construct a neural network for classifying traffic signs based on images. The German Traffic Sign Recognition Benchmark (GTSRB) dataset will be utilized, containing thousands of images with 43 different types of traffic signs.

### Tools

1. Download and unzip the `problema1-trafico.zip` code.
2. Download and unzip the `problema1-dataset.zip` dataset for this project.
3. Move the resulting `gtsrb` directory into the `traffic` directory.
4. Inside the `traffic` directory, execute `pip3 install -r requirements.txt` for the project's dependencies: `opencv-python` for image processing, `scikit-learn` for machine learning functions, and `tensorflow` for neural networks.

### Initialization

1. **Download Code and Dataset:**
   - Download and unzip the `problema1-trafico.zip` code.
   - Download and unzip the `problema1-dataset.zip` dataset for this project.
   - Move the resulting `gtsrb` directory into the `traffic` directory.

2. **Install Dependencies:**
   - Inside the `traffic` directory, open a terminal.
   - Execute the command `pip3 install -r requirements.txt` to install the necessary dependencies, including `opencv-python` for image processing, `scikit-learn` for machine learning functions, and `tensorflow` for neural networks.

3. **Verify Python Version:**
   - Ensure you have Python 3.10 or a higher version installed.

Now, the program is initialized, and you can proceed with running it. If you encounter any issues during initialization, please check the installation steps and ensure that the required dependencies are properly installed.

### Execution Instructions

1. **Open a Terminal:**
   - Open a terminal on your computer.

2. **Navigate to the Program Directory:**
   - Navigate to the directory containing `traffic.py` using the `cd` command. For example:
     ```bash
     cd path/to/traffic
     ```

3. **Run the Program:**
   - Execute the following command to run the program:
     ```bash
     python3 traffic.py gtsrb
     ```
     This command processes the GTSRB dataset for Traffic Sign Recognition.

4. **Optional: Save the Model (if provided):**
   - If a filename is provided as a parameter, the trained model will be saved. You can use this saved model for future predictions or evaluations.
    ```bash
     python3 traffic.py gtsrb my_model.h5 
     ```
5. **Review the Results:**
   - After the program completes, review the output to assess the model's training and evaluation results.
   - The program may display information such as loss, accuracy, and other metrics for each epoch.
   
### Using predict.py

The `predict.py` script allows you to make predictions on new images using a pre-trained Traffic Sign Recognition model.

### Execution Instructions

1. **Open a Terminal:**
   - Open a terminal on your computer.

2. **Navigate to the Program Directory:**
   - Navigate to the directory containing `predict.py` using the `cd` command. For example:
     ```bash
     cd path/to/traffic
     ```

3. **Run the Prediction Script:**
   - Execute the following command to run the prediction script:
     ```bash
     python3 predict.py path/to/your/image.jpg my_model.h5
     ```
     Replace `path/to/your/image.jpg` with the path to the image you want to predict, and `my_model.h5` with the filename of your pre-trained model.

4. **Review the Prediction:**
   - The script will display the predicted class and the corresponding traffic sign label for the provided image.

5. **Repeat for Multiple Images:**
   - You can repeat the process for multiple images by changing the path to different image files.
   
### Conclusion

The Traffic Sign Recognition project employs a neural network to effectively classify diverse traffic signs, demonstrating its potential for enhancing road safety in autonomous vehicles. The model's accuracy and loss metrics during training highlight its robust performance. While the current implementation is successful, ongoing optimization efforts can further refine and adapt the model for real-world traffic scenarios.

